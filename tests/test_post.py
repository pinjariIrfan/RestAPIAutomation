import json
import pytest
from utils import api_client
from utils.validators import validate_status_code, validate_response_time

with open("data/payloads.json") as f:
    PAYLOADS = json.load(f)

@pytest.mark.parametrize("payload", PAYLOADS["create_post"])
def test_create_post(payload):
    response = api_client.post("/posts", payload)
    validate_status_code(response, 201)
    validate_response_time(response)
    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data