"""
test_permissions.py — fixture chain tests for UserDB login and permissions.
Demonstrates: fixture dependency, parametrize + fixture combined, markers.
"""
import pytest
from src.validators import UserDB


# ── Login tests ────────────────────────────────────────────────────────────────

@pytest.mark.smoke
@pytest.mark.parametrize("username, expected", [
    pytest.param("ahmed",   True,  id="valid_adult_active"),
    pytest.param("sara",    False, id="invalid_underage"),
    pytest.param("khaled",  False, id="invalid_inactive"),
    pytest.param("unknown", False, id="invalid_not_found"),
])
def test_can_login(db, username, expected):
    assert db.can_login(username) == expected


# ── Permission tests ───────────────────────────────────────────────────────────

@pytest.mark.regression
@pytest.mark.parametrize("permission", ["read", "write", "delete"])
def test_admin_has_permission(admin_permissions, permission):
    assert permission in admin_permissions


@pytest.mark.regression
@pytest.mark.parametrize("username, expected_permissions", [
    pytest.param("ahmed",  ["read", "write", "delete"], id="admin_full_access"),
    pytest.param("khaled", ["read", "write"],           id="editor_partial_access"),
    pytest.param("sara",   ["read"],                    id="viewer_read_only"),
    pytest.param("ghost",  [],                          id="unknown_no_access"),
])
def test_user_permissions(db, username, expected_permissions):
    assert db.get_permissions(username) == expected_permissions
