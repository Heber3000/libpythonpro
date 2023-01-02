from libpythonpro import github_api
from unittest.mock import Mock



def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {'login': 'Heber3000', 'id': 68865710, 'node_id': 'MDQ6VXNlcjY4ODY1NzEw',
                                   'avatar_url': 'https://avatars.githubusercontent.com/u/68865710?v=4',
                                   }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('Heber3000')
    assert 'https://avatars.githubusercontent.com/u/68865710?v=4' == url

