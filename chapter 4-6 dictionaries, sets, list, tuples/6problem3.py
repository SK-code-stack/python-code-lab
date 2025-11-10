# detect that if the salman is present in the post

post = "hlo my name is Salman Khan and i am learnng python."

user = input("Enter Salman : ")
if user.lower() in post.lower():
    print("salman is present in the post")
else:
    print("salman is not present in the post")

