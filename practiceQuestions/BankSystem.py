# bank system with deposit , withdrawl and balance display function and save it in text file

# dictionary to store users (unique id : data)
users = [
    {"id": 123, "pass": 123123, "name": "salman", "balance": 100000},
    {"id": 124, "pass": 123123, "name": "ali", "balance": 20000},
]


class Bank:
    def __init__(self, user_id, user_pass):
        self.user_id = user_id
        self.user_pass = user_pass

    def register_user(self):

        user = next((u for u in users if u["id"] == self.user_id and u["pass"] == self.user_pass), None)
        if user:
            print(f"welcome{user["name"]}")

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
            user_id = int(input("Enter your user id : "))
            user_pass = int(input("Enter your password : "))
            b = Bank(user_id, user_pass) # ---------------------------------here its not good approch

            b.register_user()


        elif(choice1 == 2):
            b.register_new_user()
        elif(choice1 == 3):
            b.delete_user()
        elif(choice1 == 4):
            break


    except Exception as e:
        print(e)



    
