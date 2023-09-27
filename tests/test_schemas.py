import pytest
from pydantic import ValidationError
from apps.src.schema import Users

# Modelo padrão de testes baseados na doc do fastapi
def test_users_model_valid():
    # Teste que deve passar, fornecendo dados válidos
    user_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "password123",
        "cpf": "123456789"
    }
    user = Users(**user_data)
    assert user

def test_users_model_invalid():
    # Teste que deve falhar, fornecendo dados inválidos (falta o campo "name")
    user_data = {
        "email": "john@example.com",
        "password": "password123",
        "cpf": "123456789"
    }
    with pytest.raises(ValidationError):
        Users(**user_data)

if __name__ == "__main__":
    pytest.main()
