from random import randint


class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"Ticket is booked in train no {self.trainNo} {fro} -- {to}")
    
    def status(self, fro, to):
        print(f"Ticket is booked in train no {self.trainNo} {fro} -- {to} status OK")

    def fare(self, fro, to):
        print(f"Ticket is booked in train no {self.trainNo} {fro} -- {to} and your total fare is {randint(111,222)}")


t = Train(121222)

t.book("rajistan", "haji camp")
t.status("rajistan", "haji camp")
t.fare("rajistan", "haji camp")