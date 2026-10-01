from prash.server import app
from fastapi.testclient import TestClient

REQUIRED = [
    "x-content-type-options", "x-frame-options", "strict-transport-security",
    "content-security-policy", "referrer-policy", "permissions-policy",
]

client = TestClient(app)


def test_security_headers_on_json_response():
    response = client.get("/api/system/version")
    assert response.status_code == 200
    assert all(header in response.headers for header in REQUIRED)


def test_security_header_values():
    headers = client.get("/api/system/version").headers
    assert headers["x-content-type-options"] == "nosniff"
    assert headers["x-frame-options"] == "DENY"
    assert "max-age=31536000" in headers["strict-transport-security"]
    assert "connect-src 'self' ws: wss:" in headers["content-security-policy"]
    assert headers["referrer-policy"] == "strict-origin-when-cross-origin"
    assert headers["permissions-policy"] == "camera=(), microphone=(), geolocation=()"


def test_security_headers_on_404():
    response = client.get("/route-that-does-not-exist")
    assert response.status_code == 404
    assert all(header in response.headers for header in REQUIRED)
