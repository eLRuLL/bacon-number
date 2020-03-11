from flask import current_app, g
from neo4j import GraphDatabase


def get_db():
    if 'db' not in g:
        g.db = GraphDatabase.driver(
            current_app.config['DATABASE_URL'],
            # auth=(current_app.config['DATABASE_USERNAME'], current_app.config['DATABASE_PASSWORD']),
            encrypted=False,
        )

    return g.db


def get_db_session():
    neo4j_db = get_db()
    return neo4j_db.session()


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    """Register database functions with the Flask app. This is called by the application factory."""
    app.teardown_appcontext(close_db)
