a = input("Please enter your first value ")
b = input("please enter your second value ")

a = float(a)
b = float(b)

operator = input("Please choose which operation you would like to use? , + , - , * , /")

if operator == "+":
    answer = a + b
    print(answer)

elif operator == "-":
    answer = a - b
    print(answer)

elif operator == "*":
    answer = a * b
    print(answer)

elif operator == "/":
    answer = a / b
    print(answer)

    