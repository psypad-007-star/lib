import json
import os

DB_FILE = "users.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# --- CRUD Examples ---

# Create / Update
db = load_db()
db["user_1"] = {"name": "Alice", "role": "admin"}
db["user_2"] = {"name": "bob", "role": "user"}
save_db(db)

# Read
db = load_db()
print(db.get("user_1"))

# Delete
if "user_1" in db:
    del db["user_1"]
    save_db(db)