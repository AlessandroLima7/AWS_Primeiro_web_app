
SECRET_KEY = 'cadastroDeProdutos'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = '',
        senha = '',
        servidor = '',
        database = 'testes_bd'
    )
