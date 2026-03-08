"""
conftest.py — shared fixtures available to all test files.
"""
import pytest
from src.validators import UserDB


# --- autouse: logs every test name automatically ---
@pytest.fixture(autouse=True)
def log_test(request):
    print(f"\n▶  {request.node.name}")
    yield
    print(f"✓  done")


# --- base DB fixture ---
@pytest.fixture
def db():
    """Fresh UserDB instance for each test."""
    return UserDB()


# --- fixture chain: depends on db ---
@pytest.fixture
def admin_permissions(db):
    """Returns permissions for the admin user."""
    return db.get_permissions("ahmed")
