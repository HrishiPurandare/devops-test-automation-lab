import os

import requests

BASE = os.getenv("APP_URL", "http://app:5000")


def test_health_is_ok():
    resp = requests.get(f"{BASE}/api/health", timeout=5)
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_unknown_route_returns_404():
    assert requests.get(f"{BASE}/api/missing", timeout=5).status_code == 404
