import pytest
from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

#testing root route
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Blog API"}

#testing create post
def test_create_post():
    post_data = {"title": "Test Post", "content": "This is a test", "author": "John"}
    response = client.post("/posts/", json=post_data)
    assert response.status_code == 201
