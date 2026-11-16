from ABC inport ABC, abstract

class library:
    master_store = {
        {"author":"title"},
        {}
    }

    def __init__(self, author, title):
        self.author = author
        self.title = title

    @abstract
    def update_db(): ...

    def __string__(self):
        return f"{self.title} by {self.author}"

class intermediary(library):
    self.available = True

    def borrow(self):
        self.available = False
    

class user(library):
    def borrow():
        pass
    
    def due():
        pass
    
    def 
