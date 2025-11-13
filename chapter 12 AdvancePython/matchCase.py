# similar to switch statements 
# program to check grages
def check(grade):
    match(grade):
        case 100:
            return "A+"
        case 90:
            return "A"
        case 70:
            return "B"
        case 50:
            return "C"
        case _:
            return "Fail"
        
print(check(90))