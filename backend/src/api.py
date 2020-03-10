from flask import Blueprint
from src.db import get_db

bp = Blueprint('api', __name__)


path_query = """
MATCH path=shortestPath((from_person:Person {{name:"{from_name}"}})-[*]-(to_person:Person {{name:"{to_name}"}})) RETURN path
"""

output_movie_fields = ['id', 'imdb_id', 'title', 'poster_path', 'release_date']


def get_single_result(session, query, var_name):
    results = session.run(query)
    single_result = results.single()
    if single_result:
        return single_result[var_name]


@bp.route('/<from_name>/<to_name>')
def index(from_name, to_name):
    response = {
        'number': 0,
        'movies': [],
        'people': [],
        'connections': [],
    }
    if from_name == to_name:
        return response

    neo4j_db = get_db()
    with neo4j_db.session() as session:
        path_result = get_single_result(session, path_query.format(from_name=from_name, to_name=to_name), 'path')
        if not path_result:
            return response
        for relation in path_result.relationships:
            response['connections'].append((relation.start_node['id'], relation.type, relation.end_node['id']))

        for graph_node in path_result.nodes:
            if 'Person' in graph_node.labels:
                response['people'].append(dict(graph_node))
            elif 'Movie' in graph_node.labels:
                dict_movie = {}
                for field in output_movie_fields:
                    if field in graph_node:
                        dict_movie[field] = str(graph_node[field])
                response['movies'].append(dict_movie)
            else:
                raise Exception('not supported node label: %s' % graph_node.labels)

        response['number'] = len(response['movies'])

    return response
