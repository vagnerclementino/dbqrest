import requests


def test_get_all_collections():
    """TODO: Docstring for test_get_all_collections.
    :returns: TODO

    """
    url = 'http://127.0.0.1:5000/api/person'
    headers = {'Accept': 'application/vnd.api+json'}

    # Make a GET request for the entire collection.
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.json())
