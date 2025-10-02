import pytest
from application import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_error_code(client):
    response = client.get('/error/404')
    assert response.status_code == 404
    assert response.is_json

def test_user_info(client):
    response = client.get('/user/testuser')
    assert response.status_code in [200, 404]