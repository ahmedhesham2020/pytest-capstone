"""
Validators — functions under test.
Covers: password validation, age validation, user permissions.
"""


def is_valid_password(password: str) -> bool:
    """Returns True if password length is between 8 and 20 characters."""
    return 8 <= len(password) <= 20


def is_valid_age(age: int) -> bool:
    """Returns True if age is between 18 and 99 inclusive."""
    return 18 <= age <= 99


def divide(a: float, b: float) -> float:
    """Divides a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class UserDB:
    """Fake user database for permission testing."""

    def __init__(self):
        self._users = {
            "ahmed":  {"age": 25, "active": True,  "role": "admin"},
            "sara":   {"age": 17, "active": True,  "role": "viewer"},
            "khaled": {"age": 30, "active": False, "role": "editor"},
        }

    def get_user(self, username: str) -> dict | None:
        return self._users.get(username)

    def can_login(self, username: str) -> bool:
        user = self.get_user(username)
        if user is None:
            return False
        return user["active"] and user["age"] >= 18

    def get_permissions(self, username: str) -> list:
        user = self.get_user(username)
        if user is None:
            return []
        role_map = {
            "admin":  ["read", "write", "delete"],
            "editor": ["read", "write"],
            "viewer": ["read"],
        }
        return role_map.get(user["role"], [])
