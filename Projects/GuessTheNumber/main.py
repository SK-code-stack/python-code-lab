import random

class Guess:
        
    
    def evaluate(self):
        computer = random.randint(1, 10)
        
        i = 0 
        while True:
            self.number = input("Enter a number between 1 and 10 (or 'exit' to quit): ")
            if self.number.lower() == "exit":
                break
            if not self.number.isdigit():
                print("Please enter a valid number")
                continue

            user_num = int(self.number)
            i += 1
            if user_num > 10 or user_num < 1:
                print("Enter a valid number between 1 - 10")
            elif user_num > computer:
                print("Too High guess lower")
            elif user_num < computer:
                print("Too Low guess higher")
            else:
                print(f"You won and you use {i} tries")
                break






print("Welcome to the game ")

a = Guess()
a.evaluate()

