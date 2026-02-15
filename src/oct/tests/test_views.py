import pytest
from django.test import Client


@pytest.mark.django_db
def test_oct_info_returns_platform_details():
    """OCT info endpoint returns platform metadata."""
    client = Client()
    response = client.get("/api/oct/info/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "OCT"
    assert "West Africa" in data["tagline"]
    assert "banking" in data["stakeholders"]
