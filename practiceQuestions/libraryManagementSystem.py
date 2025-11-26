# Library Management System –
#Build a class Book (title, author, available_copies) and Library to:

import json

class book:
    def __init__(self):
        try:
            with open("library.json", "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []
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


    def addBook(self):
        print("Enter Book Detailes")
        bookName = input("Enter title of the book : ")
        authorName = input("Enter author name of the book : ")
        noCopies = int(input("Enter number of copies of the book : ")) # number of copies 
        book = next((u for u in self.books if u["author"] == str(authorName) and u["title"] == str(bookName)), None)

        if book:
            book["copies"] =  book["copies"]  + noCopies
        else:
            self.books.append({"author":authorName, "title":bookName,  "copies":noCopies},)
        with open("library.json", "w") as file:
            json.dump(self.books, file, indent=4)

        print(self.books)

    def borrowBook(self):
        print("Enter details of the book that you want to borrow")
        bookName = input("Enter name of the book : ")
        authorName = input("Enter name of the author : ")
        book = next((b for b in self.books if b["title"] == str(bookName) and b["author"] == str(authorName)), None)
        if not book:
            print("NO book is availble with this name and author")
        elif book:
            book["copies"] == str(0)
            book["copies"] -= 1
            print("book alloted successfully")
            with open("library.json", "w") as file:
                json.dump(self.books, file, indent=4)

            print(self.books)

    def returnBook(self):
        print("boook is returned")
        pass



b = book()
b.choice() 