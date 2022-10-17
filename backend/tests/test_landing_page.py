import pytest
from backend.routes import app
import json

#### Setup #####
@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
################

def test_SUCCESS_GET():
    response = app.test_client().get('/')

    # Assert 
    assert response.status_code == 200
