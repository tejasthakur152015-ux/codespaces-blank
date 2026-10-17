# clculater
# loops project




options = (" *, /, +, -")
print(options)
player = input("enter a operater")
if player not in options:
    print("erorr")
    
if player == "+":
    number_1 = int(input("enter a number:"))
    number_2 = int(input("enter your second number:"))
    sum = number_1 + number_2
    print(sum)
elif player == "*":
    number_1 = int(input("enter a number:"))
    number_2 = int(input("enter your second nomber:"))
    sum = number_1 * number_2
    print(sum)
elif player == "-":
    number_1 = int(input(" enter a number: "))
    number_2 = int(input("enter your secound number:"))
    sum = number_1 - number_2
    print(sum)
elif player == "/":
    number_1 = int (input("enter a number:"))
    number_2 = int(input("enter your secom=nd number:"))
    sum = number_1 / number_2
    print(sum)
    

    
