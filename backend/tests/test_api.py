from unittest import mock


def test_same_name(client, random_name):
    """Test same name gives back an empty response."""
    test_name = random_name()
    response = client.get(f'/{test_name}/{test_name}')
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['number'] == 0


@mock.patch('src.api.get_db_session')
@mock.patch('src.api.get_single_result')
def test_empty_result(single_result, _, client, random_name):
    """Test no results from database gives back an empty response."""
    single_result.return_value = None
    response = client.get(f'/{random_name()}/{random_name()}')
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['number'] == 0


@mock.patch('src.api.get_db_session')
@mock.patch('src.api.get_single_result')
def test_get_result(single_result, _, client, random_name, mock_path):
    """Test response with actual results from the db."""
    single_result.return_value = mock_path(relations=5)
    response = client.get(f'/{random_name()}/{random_name()}')
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['number'] == 5
