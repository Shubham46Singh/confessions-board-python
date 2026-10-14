
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_invalid_moderation_action_returns_400():
    response = client.post(
        "/moderation/1",
        json={"action": "invalid"}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "action must be 'approve' or 'reject'"
    )


def test_missing_moderation_action_returns_400():
    response = client.post(
        "/moderation/1",
        json={}
    )

    assert response.status_code == 400
