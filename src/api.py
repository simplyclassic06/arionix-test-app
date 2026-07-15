from auth import verify_password, generate_token

users_db = {}

def register_user(email: str, password: str) -> dict:
    if email in users_db:
        return {"error": "User already exists"}
    users_db[email] = password
    return {"message": "User registered successfully"}

def login(email: str, password: str) -> dict:
    if email not in users_db:
        return {"error": "User not found"}
    if not verify_password(password, users_db[email]):
        return {"error": "Invalid password"}
    token = generate_token(email)
    return {"token": token}

def get_user(email: str) -> dict:
    if email not in users_db:
        return {"error": "User not found"}
    return {"email": email}
