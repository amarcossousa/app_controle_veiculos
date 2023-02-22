from fastapi.testclient import TestClient


def test_create_user_sucess(client: TestClient) -> None:
   response = client.post('/user/', json=
      {
    "id": 0,
    "name": "string",
    "email": "user@example.com",
    "phone_number": "string",
    "password": "string"
      }
   )
   assert response.status_code == 201