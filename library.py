class Library:
    def __init__(self, book):
        self.book = book
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            print("Checked out")
        else:
            print("Not available")
