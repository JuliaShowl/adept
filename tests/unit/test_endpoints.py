import sys, os, json

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


def test_update():
    invalid_status = app.test_client().put('/documents/1', data={'status': 'test'}, headers={'Content-Type': 'application/json', 'charset': 'utf-8'})
    invalid_doc = app.test_client().put('/documents/7', data={'status': 'In Review'}, headers={'Content-Type': 'application/json', 'charset': 'utf-8'})
    invalid_payload = app.test_client().put('/documents/7', headers={'Content-Type': 'application/json', 'charset': 'utf-8'})
    assert invalid_status.status_code == 400
    assert invalid_doc.status_code == 400
    assert invalid_payload.status_code == 400
