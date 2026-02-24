import requests
import time

BASE_URL = "https://jsonplaceholder.typicode.com"

def get(endpoint, params=None):
    start = time.time()
    response = requests.get(f"{BASE_URL}{endpoint}", params=params)
    response.elapsed_custom = time.time() - start
    return response

def post(endpoint, payload):
    start = time.time()
    response = requests.post(f"{BASE_URL}{endpoint}", json=payload)
    response.elapsed_custom = time.time() - start
    return response

def put(endpoint, payload):
    start = time.time()
    response = requests.put(f"{BASE_URL}{endpoint}", json=payload)
    response.elapsed_custom = time.time() - start
    return response

def delete(endpoint):
    start = time.time()
    response = requests.delete(f"{BASE_URL}{endpoint}")
    response.elapsed_custom = time.time() - start
    return response