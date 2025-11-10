# checking that the given number is prime or not 

user = int(input("Enter the number : "))
 
for i in range(2, user):
    if (user%i) == 0:
        print("its not prime ")
        break
    else:
        print("its  prime ")
        break
