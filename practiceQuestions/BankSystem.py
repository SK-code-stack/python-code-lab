# bank system with deposit , withdrawl and balance display function and save it in text file

class Bank:
    def __init__(self):

        pass

    def register_user(self):
        user_id = int(input("Enter your user id : "))
        user_pass = int(input("Enter your password"))
        # ---------------------------------------------------------yaha sa krna hai yaha password validate krana hai
        print("hlo")

    def register_new_user(self):
        print("hlo")

    def delete_user(self):
        pass

    def deposit(self):
        pass

    def withdrawl(self):
        pass

    def display_balance(self):
        pass




b = Bank()

# dictionary to store users (unique id : data)
users = {
    123 : {"pass":123123,"name":"salman", "balance":100000},
    124 : {"pass":123123,"name":"ali", "balance":20000},
}

print("Bank Management System")

while True:
    try:
        print('''
            1 - Register User
            2 - Create an account
            3 - Delete account 
            4 - Exit
        ''')
        choice1 = int(input("Enter your choice "))


        if (choice1 < 1 or choice1 > 4):
            print("Invalid choice please select from the given menu")
        elif (choice1 == 1):
            b.register_user()
        elif(choice1 == 2):
            b.register_new_user()
        elif(choice1 == 3):
            b.delete_user()
        elif(choice1 == 4):
            break


    except Exception as e:
        print(e)



    
