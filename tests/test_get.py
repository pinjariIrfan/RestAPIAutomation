import pytest
from utils import api_client
from utils.validators import validate_status_code, validate_response_time, validate_json_schema

POST_SCHEMA = {
    "type": "object",
    "required": ["id", "title", "body", "userId"],
    "properties": {
        "id":     {"type": "integer"},
        "title":  {"type": "string"},
        "body":   {"type": "string"},
        "userId": {"type": "integer"}
    }
}

def test_get_all_posts():
    response = api_client.get("/posts")
    validate_status_code(response, 200)
    validate_response_time(response)
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_single_post():
    response = api_client.get("/posts/1")
    validate_status_code(response, 200)
    validate_response_time(response)
    validate_json_schema(response.json(), POST_SCHEMA)

def test_get_invalid_post():
    response = api_client.get("/posts/99999")
    validate_status_code(response, 404)