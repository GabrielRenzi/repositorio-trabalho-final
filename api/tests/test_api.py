import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Teste 1: Obrigatório - HTTP 200 para a rota GET /[recurso]
def test_get_videos_returns_200(client):
    response = client.get('/videos')
    assert response.status_code == 200

# Teste 2: Obrigatório - Validação da estrutura JSON
def test_get_videos_structure(client):
    response = client.get('/videos')
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 10
    assert "id" in data[0]
    assert "titulo" in data[0]

# Teste 3: Obrigatório - HTTP 404 para identificador inexistente
def test_get_video_not_found(client):
    response = client.get('/videos/9999')
    assert response.status_code == 404

# Teste 4: Autoria própria - Validar a rota /status
def test_status_route(client):
    response = client.get('/status')
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "online"