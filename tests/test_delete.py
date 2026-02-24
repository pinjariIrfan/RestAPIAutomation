from utils import api_client
from utils.validators import validate_status_code, validate_response_time

def test_delete_post():
    response = api_client.delete("/posts/1")
    validate_status_code(response, 200)
    validate_response_time(response)
    assert response.json() == {}

def test_delete_invalid_post():
    response = api_client.delete("/posts/99999")
    validate_status_code(response, 200)
    validate_response_time(response)