users = {
    "alice": {"password": "admin123", "role": "admin"},
    "bob": {"password": "eng123", "role": "engineer"},
    "carol": {"password": "audit123", "role": "auditor"}
}

permissions = {
    "admin": ["read", "write", "delete"],
    "engineer": ["read", "write"],
    "auditor": ["read"]
}

def authenticate(username, password):
    user = users.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None

def check_access(role, action):
    return action in permissions.get(role, [])

# Demo
role = authenticate("bob", "eng123")

if role:
    print("Authenticated as:", role)
    print("Can write?", check_access(role, "write"))
    print("Can delete?", check_access(role, "delete"))
else:
    print("Authentication failed")
