# it helps you to assign variables even in the statements conditions

if (n := len([1,2,3,4,5])) > 3:
    print(f"you have list of length {n} and expected legth is 3")


# types (its not necessory but it helps you to make code readable)
def sum(a : int, b : int) -> int: # this says that a and b are intiger and returning -> intiger
    return a+b

sum(2, 3)


