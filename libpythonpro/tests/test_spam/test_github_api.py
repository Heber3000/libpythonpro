from libpythonpro import github_api
from unittest.mock import Mock
import pytest


@pytest.fixture()
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/68865710?v=4'
    resp_mock.json.return_value = {'login': 'Heber3000', 'id': 68865710, 'node_id': 'MDQ6VXNlcjY4ODY1NzEw',
                                   'avatar_url': url,
                                   }
    get_mock=mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock

    return url

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('Heber3000')
    assert avatar_url == url



def test_buscar_avatar_integracao():

    url = github_api.buscar_avatar('Heber3000')
    assert 'https://avatars.githubusercontent.com/u/68865710?v=4' == url

