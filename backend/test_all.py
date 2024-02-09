import pytest
from fastapi.testclient import TestClient
from backend.main import app

print("🚀 Testing the FastAPI backend!")


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_read_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Server": "Running"}
    print("✅ Test passed like a charm for root!")

@pytest.mark.filterwarnings("ignore:The `dict`")
def test_anonymyze(test_client):
    input_text = "Hello World!"
    response = test_client.post("/api/anonymyze", params={"input_text": input_text})
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 3
    assert len(response_json["anonymyzed_text"]) > 1
    assert len(response_json["deanonymyzed_text"]) > 1
    print(f"✅ Tests passed like a charm for input_text: {input_text}!")
