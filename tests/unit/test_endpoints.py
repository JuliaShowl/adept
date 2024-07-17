from conftest import client

def test_status_codes():
    user = client.get('/user')
    stats = client.get('/stats')
    documents = client.get('/documents')
    assert user.status_code == 200
    assert stats.status_code == 200
    assert documents.status_code == 200