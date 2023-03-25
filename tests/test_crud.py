from apps.src import schema
import pytest

@pytest.fixture
def test_create_user(self):
    # Cria um usuário de teste
    user = schema.Users(name="John Doe", email="john.doe@example.com", password="password")

    # Chama a função create_user para adicionar o usuário ao banco de dados
    db_user = self.crud_users.create_user(user)

    # Verifica se o usuário foi adicionado corretamente
    assert db_user.id is not None
    assert db_user.name == "John Doe"
    assert db_user.email == "john.doe@example.com"
    assert db_user.password == "password"

    # Verifica se o usuário pode ser recuperado pelo e-mail
    db_user_by_email = self.crud_users.get_user_by_email("john.doe@example.com")
    assert db_user_by_email is not None
    assert db_user_by_email.id == db_user.id
    assert db_user_by_email.name == "John Doe"
    assert db_user_by_email.email == "john.doe@example.com"
    assert db_user_by_email.password == "password"
