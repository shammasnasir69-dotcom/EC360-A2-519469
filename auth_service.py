
import hashlib
import os

users = {}

def register_user(email, password):
    if email in users:
        return "User already exists"

    if len(password) < 12:
        return "Password must be at least 12 characters"

    salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt, 100000
    )

    users[email] = {
        "salt": salt.hex(),
        "password_hash": password_hash.hex()
    }

    return "Registration successful"
