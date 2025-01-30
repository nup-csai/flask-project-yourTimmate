import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_redirect(client):
    """Тест проверяет, что неавторизованный пользователь перенаправляется на /login"""
    response = client.get('/')
    assert response.status_code == 302
    assert '/login' in response.headers['Location']

def test_login_page(client):
    """Тест проверяет доступность страницы логина"""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_successful_login(client):
    """Тест проверяет успешный вход в систему"""
    response = client.post('/login', data={'username': 'Burner', 'password': 'Tickets'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Burning Man' in response.data

def test_failed_login(client):
    """Тест проверяет ошибку при вводе неправильных учетных данных"""
    response = client.post('/login', data={'username': 'WrongUser', 'password': 'WrongPass'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Invalid credentials' in response.data

def test_logout(client):
    """Тест проверяет выход из системы"""
    client.post('/login', data={'username': 'Burner', 'password': 'Tickets'}, follow_redirects=True)
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data
