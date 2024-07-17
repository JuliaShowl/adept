import sys, os

parent_directory = os.path.abspath('../../')
sys.path.append(parent_directory)

from backend.app import app 

def test_status_codes():
    user = app.test_client().get('/user')
    stats = app.test_client().get('/stats')
    documents = app.test_client().get('/documents')
    assert user.status_code == 200
    assert stats.status_code == 200
    assert documents.status_code == 200