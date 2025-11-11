# Check if a given string or number is a palindrome.
a = input("Enter a word : ")
rstr = ''.join(reversed(a))

if (a == rstr):
    print("Its paladrom")
else:
    print("Its not paladrom")
