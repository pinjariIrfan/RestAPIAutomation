import json
import pytest
from utils import api_client
from utils.validators import validate_status_code, validate_response_time

with open("data/payloads.json") as f:
    PAYLOADS = json.load(f)

@pytest.mark.parametrize("payload", PAYLOADS["update_post"])
def test_update_post(payload):
    response = api_client.put(f"/posts/{payload['id']}", payload)
    validate_status_code(response, 200)
    validate_response_time(response)
    assert response.json()["title"] == payload["title"]