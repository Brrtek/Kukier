class Library(): 
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): 
        if requestedBook in self.availableBooks: 
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): 
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): 
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")

class Customer(): 
    book = ""
    haveBook = False
    def requestBook(self, book): 
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False

def setup():
    size(220,100)
    global library, Bartek
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Trupia Farma"]
    library = Library(books) 
    Bartek = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) # do wypożyczania
    rect(100,40,100,20) # do zwracania
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)

def mouseClicked():  
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Bartek.requestBook("Trupia Farma")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Bartek.returnBook())
            
import unittest

class Test(unittest.TestCase):
    
    def test_alfabetycznie(self): # zapomniałam podkreślić, że nazwa testu musi się zaczynać od test...
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Trupia Farma"]
        result = sorted(books)
        self.assertEqual(result, ["Harry Potter", "Naocznosc", "Sens Sztuki", "Trupia Farma"])
        
    def test_ilosc(self):
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Trupia Farma"]
        result = len(books)
        self.assertEqual(result, 4)
        
if __name__ == '__main__':
    unittest.main()
    
# w testach nie używasz klas z kodu, a więc testujesz nie kod, a wbudowane metody pythona
# 1,5pkt
