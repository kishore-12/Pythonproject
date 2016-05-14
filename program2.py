num = int(input("enter a num for factorial="))

factorial = 1
if num < 0:
    print(" doen't exit")
elif num == 0:
    print(" fact of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(" factorial of ", num, "is", factorial)
