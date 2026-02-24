import jsonschema

def validate_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f"Expected {expected_code}, got {response.status_code}"

def validate_response_time(response, max_seconds=2.0):
    elapsed = response.elapsed.total_seconds()
    assert elapsed < max_seconds, \
        f"Response too slow: {elapsed:.2f}s (max {max_seconds}s)"

def validate_json_schema(response_json, schema):
    jsonschema.validate(instance=response_json, schema=schema)