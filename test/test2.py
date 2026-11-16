import json
import os

DB_FILE = "library_db.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {"books": {}, "members": {}}
    with open(DB_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# --- Library Functions ---

def add_book(book_id, title, author, number_available):
    db = load_db()
    db["books"][book_id] = {
        "title": title,
        "author": author,
        "number": number_available,
    }
    save_db(db)

def borrow_book(book_id):
    db = load_db()
    if book_id in db["books"] and db["books"][book_id]["number"]:
        db["books"][book_id]["number"] -= 1
        save_db(db)
        print(f"Book '{db['books'][book_id]['title']}' checked out.")
    else:
        print("Book is unavailable or does not exist.")

# --- Example Usage ---
add_book("B001", "The Pragmatic Programmer", "Andrew Hunt", 2)
add_book("B002", "Clean Code", "Robert C. Martin", 4)
borrow_book("B001")