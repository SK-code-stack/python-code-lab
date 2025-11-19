# bank system with deposit , withdrawl and balance display function and save it in text file




class Bank:
    def __init__(self):
        self.users = [
            # {"id": 123, "pass": 123123, "name": "salman", "balance": 100000},
            # {"id": 124, "pass": 123123, "name": "ali", "balance": 20000},
        ]
        self.current_user = None
        if self.users == []:
            self.last_id = 0
        else:
            self.last_id = max(user["id"] for user in self.users)




    def choices(self):
        print("Bank Management System")
        while True:
            try:
                print('''
                    1 - Login 
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

                    self.login(user_id, user_pass)

                elif(choice1 == 2):
                    self.register_new_user()

                elif(choice1 == 3):
                    self.delete_user()

                elif(choice1 == 4):
                    break


            except Exception as e:
                print(e)




    def login(self, user_id, user_pass):
 
        user = next((u for u in self.users if u["id"] == user_id and u["pass"] == user_pass), None)
        self.current_user = user
        if user:
            print("--------------------------------------------")
            print(f"welcome {user['name']}")
            while True:
                print('''
                    1 - Display Balance
                    2 - Withdrawal
                    3 - Deposit
                    4 - Exit
                ''')
                choice2 = int(input("Enter your choice : "))

                if (choice2 < 1 or choice2 > 4):
                    print("Invalid choice please select from the given menu")
                elif (choice2 == 1):
                    self.display_balance()
                elif (choice2 == 2):
                    self.withdrawl()
                elif (choice2 == 3):
                    self.deposit()
                elif (choice2 == 4):
                    break
        else:
            print("User id and password does not matched.")
            

    def register_new_user(self):
        print("Welcome to digiBank provide the following information.")
        id = self.last_id + 1
        name = input("Enter your full name : ")
        user_pass = int(input("Enter password: "))
        confirm_pass = int(input("Confirm your password: "))
        if user_pass == confirm_pass:
            # adding this info to the users list
            self.users.append({"id": id, "pass": user_pass, "name": name.title(), "balance": 0})
            print(f"{name.title()} your account is created and your login id is {id} please note it carefully.")
        else:
            print("Password and confirm password are not same")




    def delete_user(self):
        pass

    def deposit(self):
        pass

    def withdrawl(self):
        pass

    def deposit(self):
        pass

    def display_balance(self):
        balance = self.current_user["balance"]
        name = self.current_user["name"]
        print(f"{name.title()} your balance is {balance} Rs")
        pass




b = Bank()

b.choices()
