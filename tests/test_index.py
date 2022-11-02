import requests


def test_index():
    response = requests.get("http://44.201.64.128:5000/")
    assert response.status_code == 200
