import requests
import json


def test_get():
    """TODO: Docstring for test_get_all_collections.
    :returns: TODO

    """
    collections = ['questions', 'choices']
    headers = {'accept': 'application/vnd.api+json'}
    post_headers = {'Accept': 'application/json',
                    'Content-Type': 'application/json'
                   }

    question = {"description": "Quem nasceu primeiro, o ovo ou a galinha?",
                  "choices" : [{"description": "O ovo",
                                "answer": "N"
                                },

                               {"description": "A galinha",
                                "answer": "N"
                                },

                               {"description": "O Sarney",
                                "answer": "N"
                                },

                               {"description": "Todas as opções anteriores",
                                "answer": "N"
                                },
                              ]
    }

    url = 'http://127.0.0.1:5000/api/v1/%s' % collections[0]
    response = requests.post(url,
                             data=json.dumps(question),
                             headers=post_headers
                             )
    assert response.status_code == 201

    for resource in collections:
        url = 'http://127.0.0.1:5000/api/v1/%s' % resource
        # Make a GET request for the entire collection.
        response = requests.get(url, headers=headers)
        assert response.status_code == 200

    for resource in collections:
        url = 'http://127.0.0.1:5000/api/v1/%s/1' % resource
        # Make a GET request for the entire collection.
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
