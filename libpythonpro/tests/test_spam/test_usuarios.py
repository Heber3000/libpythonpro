from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario= Usuario(nome='Heber',email='heberlevy@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuario(sessao):
    usuarios = [
                Usuario(nome='Heber',email='heberlevy@gmail.com'),
                Usuario(nome='Levy',email='hebergeologo@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
