import requests


def test_get_question():
    """TODO: Docstring for test_get_question.
    :returns: TODO

    """
    r = requests.get('http://localhost:5000/question/1')
    q_default = dict(id=1,
                     description='Quem nasceu primeiro, o ovo ou a galinha?'
                     )
    assert r.json() == q_default
