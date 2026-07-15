import hashlib
import secrets

def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return f"{salt}:{hashed}"

def verify_password(password: str, stored: str) -> bool:
    salt, hashed = stored.split(":")
    return hashlib.sha256((password + salt).encode()).hexdigest() == hashed

def generate_token(user_id: str) -> str:
    return secrets.token_hex(32)

def is_token_valid(token: str) -> bool:
    return len(token) == 64
