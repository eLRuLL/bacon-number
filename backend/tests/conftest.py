import random
import string

import pytest
from src import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """Test client for the app."""
    return app.test_client()


@pytest.fixture
def random_name():
    def _inner_name_generator():
        """Generate a random actor name."""
        letters = string.ascii_lowercase
        first_name = ''.join(random.choice(letters) for _ in range(random.randint(3, 6)))
        last_name = ''.join(random.choice(letters) for _ in range(random.randint(7, 10)))
        return f'{first_name} {last_name}'.title()
    return _inner_name_generator


class MockNode(dict):
    def __init__(self, labels, **kwargs):
        self.labels = labels
        super().__init__(**kwargs)


class MockRelation:
    def __init__(self, node1, node2):
        self.start_node = node1
        self.end_node = node2
        self.type = 'dummy'


class MockPath:
    def __init__(self, relations=1):
        self.nodes = []
        self.relationships = []
        for _ in range(relations):
            node1 = MockNode(id=random.randint(1, 100000), labels={'Person'})
            node2 = MockNode(id=random.randint(1, 100000), labels={'Movie'})
            self.nodes.append(node1)
            self.nodes.append(node2)
            self.relationships.append(MockRelation(node1, node2))


@pytest.fixture
def mock_path():
    def create_mock_path(relations=1):
        return MockPath(relations=relations)

    return create_mock_path
