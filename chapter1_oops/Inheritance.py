class LibraryResource:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book {self.title} written by {self.author}"

# Single Level Inheritance

class Book(LibraryResource):
    def __init__(self,title,author,num_pages):
        super().__init__(title,author)
        self.num_pages = num_pages

    def get_details(self):
        return f"Book {self.title} has {self.num_pages} pages been wriien by famous book author {self.author}"

# Multiple Inheritance

class Ebook(Book):
    def __init__(self,title,author,num_pages,file_mb):
        super().__init__(title,author,num_pages)
        self.file_mb = file_mb

    def get_details(self):
        return f"Book {self.title} written by of {self.author} with {self.num_pages} pages has E-book pdf of size: {self.file_mb} Mb."


ebook = Ebook("Harry Potter And The Chamber Of Secrets","JK Rowling",785,2.5)
print(ebook.get_details())