# Library Management System –
#Build a class Book (title, author, available_copies) and Library to:

import json

class book:
    def __init__(self):
        self.books = [
            {"author":"salman", "title":"science",  "copies":2},
            {"author":"ali", "title":"islam",  "copies":5},
            {"author":"asad", "title":"urdu",  "copies":0},
        ]
        pass

    def choice(self):
        print("welcome to the library")
        while True:
            print('''
                    1 - Borrow Book
                    2 - Add new Book
                    3 - Return Book
                    4 - Exit
''')
            choice = int(input("Enter your choice : "))
            if choice <= 0 or choice <= 0:
                print("Invalid choice please select from the given menu")
            elif (choice == 1):
                self.borrowBook()

            elif(choice == 2):
                self.addBook()

            elif(choice == 3):
                self.returnBook()


            elif(choice == 4):
                break

        pass

    def addBook(self):
        print("Enter Book Detailes")
        bookName = input("Enter title of the book : ")
        authorName = input("Enter author name of the book : ")
        noCopies = int(input("Enter number of copies of the book : "))
        book = next((u for u in self.books if u["author"] == str(authorName) and u["title"] == str(bookName)), None)

        if book:
            book["copies"] = noCopies
        else:
            self.books.append({"author":authorName, "title":bookName,  "cpoies":noCopies},)

        with open("library.json", "w") as file:
            json.dump(self.books, file, indent=4)

        print(self.books)
        pass

    def borrowBook(self):
        print("boook is borrowed")
        pass

    def returnBook(self):
        print("boook is returned")
        pass



b = book()
b.choice() 