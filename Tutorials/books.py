class Books():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __repr__(self):

        return f"Title: {self.title} Author: {self.author}"

mybook = Books("I love python","Raji",250)
print(mybook)