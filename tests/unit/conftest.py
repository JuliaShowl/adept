import pytest
import sys, os
parent_directory = os.path.abspath('../..')
sys.path.append(parent_directory)
from backend.app import app as application

@pytest.fixture
def app():
    yield application

@pytest.fixture
def client(app):
    return app.test_client()