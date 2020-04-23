#http://127.0.0.1:5000/
import requests

URL = "http://127.0.0.1:5000/"

def test_index():
    response = requests.get(URL)
    assert response.json() == 'I BROKE IT '
