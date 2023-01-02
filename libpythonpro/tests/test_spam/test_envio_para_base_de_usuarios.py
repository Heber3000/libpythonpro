from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
import pytest
from unittest.mock import Mock



@pytest.mark.parametrize(
    'usuarios',
    [
        [
                Usuario(nome='Heber',email='heberlevy@gmail.com'),
                Usuario(nome='Levy',email='heberlevy@gmail.com')
        ],
        [
                Usuario(nome='Heber',email='heberlevy@gmail.com')
        ]
    ]


)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao,enviador)
    enviador_de_spam.enviar_emails(
        'heberlevy@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count





def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Heber',email='heberlevy@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'hebergeologo@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'hebergeologo@gmail.com',
        'heberlevy@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
