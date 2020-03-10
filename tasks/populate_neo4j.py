import csv
import os

from neo4j.v1 import GraphDatabase

current_path = os.path.dirname(os.path.realpath(__file__))
dataset_path = os.path.join(current_path, "..", "datasets", "the-movies-dataset")

# Database Credentials
uri = "bolt://0.0.0.0:7687"
userName = "neo4j"
password = "password"

# Connect to the neo4j database server
driver = GraphDatabase.driver(uri, auth=(userName, password), encrypted=False)


people_query = f"""
LOAD CSV WITH HEADERS FROM "file:///datasets/the-movies-dataset/people.csv" AS row
CREATE (n:Person)
SET n = row,
n.id = toInteger(row.id),
n.gender = toInteger(row.gender)  
"""

movies_query = f"""
LOAD CSV WITH HEADERS FROM "file:///datasets/the-movies-dataset/movies_metadata.csv" AS row
CREATE (n:Movie)
SET n = row,
n.adult = toBoolean(row.adult),
n.budget = toFloat(row.budget),
n.id = toInteger(row.id),
n.popularity = toFloat(row.popularity),
n.release_date = CASE row.release_date WHEN "1" THEN null WHEN "12" THEN null WHEN "22" THEN null WHEN "" THEN null ELSE date(row.release_date) END,
n.revenue = toFloat(row.revenue),
n.runtime = toFloat(row.runtime),
n.video = toBoolean(row.video),
n.vote_average = toFloat(row.vote_average),
n.vote_count = toFloat(row.vote_count)
"""


with driver.session() as session:
    session.run(people_query)
    print("people created", flush=True)
    session.run(movies_query)
    print("movies created", flush=True)
    session.run("CREATE INDEX ON :Person(id)")
    session.run("CREATE INDEX ON :Movie(id)")
    print('indices created', flush=True)

    with open(os.path.join(dataset_path, 'credits.csv')) as credits_file:
        reader = csv.DictReader(credits_file)
        for i, row in enumerate(reader):
            cast = eval(row.get('cast', '[]'))
            actor_ids = [person['id'] for person in cast]
            if actor_ids:
                session.run(f"MATCH (p:Person), (m:Movie) WHERE p.id in {actor_ids} and m.id={row['id']} CREATE (p)-[:ACTED_IN]->(m)")
            print(f'movies connected: {i}', end='\r', flush=True)
