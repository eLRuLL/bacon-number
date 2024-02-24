import os
import csv

current_path = os.path.dirname(os.path.realpath(__file__))
dataset_path = os.path.join(current_path, "..", "datasets", "the-movies-dataset")

people = {}

with open(os.path.join(dataset_path, 'credits.csv')) as credits_file:
    reader = csv.DictReader(credits_file)
    for row in reader:
        cast = eval(row.get('cast', '[]'))
        for actor in cast:
            people[actor['id']] = {
                'id': actor['id'],
                'name': actor['name'],
                'profile_path': actor['profile_path'],
                'gender': actor['gender'],
            }
        crew = eval(row.get('crew', '[]'))
        for person in crew:
            people[person['id']] = {
                'id': person['id'],
                'name': person['name'],
                'profile_path': person['profile_path'],
                'gender': person['gender'],
            }

with open(os.path.join(dataset_path, 'people.csv'), 'w', newline='') as people_file:
    writer = csv.writer(people_file)
    writer.writerow(['id', 'name', 'profile_path', 'gender'])
    for person in people.values():
        writer.writerow([person['id'], person['name'], person['profile_path'], person['gender']])
