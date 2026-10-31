from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_hello():
    response = app.test_client().get('/hello')
    assert response.status_code == 200

def test_about():
    response = app.test_client().get('/about')
    assert response.status_code == 200