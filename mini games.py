#mini games!




import random




games = ("'rock paper sicoorse', 'number gusser', 'calculater',  'dugeon', or 'dice;")
print(games)
player = input("chose a app")
running = True

while running:
    if player == 'rock paper siccorse':
        # rock paper siccorse game
# loops practice
       options = ("rock, paper, siccores")
print(options)
player = None
computer = random.choice("rock, paper, siccores")
runnning = True


while runnning:
    while player not in options:
            player = input("Enter a choice ")

            print(f" player{player}:")
            print(f" coputer {computer}:")

            if player == "rock" and computer =="rock":
                print("its a tie")
            elif player == "paper" and computer == "paper":
                print("its a tie")
            elif player == "siccores" and computer == "sicccores":
                print("its a tie")
            elif player == "rock" and computer == "paper":
                print("you lose")
            elif player ==  "siccores" and computer == "paper":
                print("you win")
            elif player == "paper" and computer == "rock":
                print("you win")
            elif player == "siccores" and computer == "rock":
                print(" you lose")
            elif player == "rock" and computer == "siccores":
                print(" you win")

                print("thanks for playing")

else:
    if player == 'number gusser':
        #number gussser
#game 1.0
#goated




     options = ("1, 2, 3, 4, 5")
computer = random.choice("1, 2, 3, 4, 5")
player = None
running = True

while running:
        print(options)
        player = int(input(" enter a choice"))
        if player == 1  and computer == 1:
            print("you win")
            print(" congratts" )
        elif player == 2 and computer == 2:
            print("you win")
            print(" congratts" )
        elif player == 3 and computer == 3:
            print("you win")
        elif player == 4 and computer == 4:
            print("you win ")
            print(" congratts" )
        elif player == 5 and computer == 5:
            print("you win")
            print(" congratts" )
        elif player == 2 and computer == 1:
            print(" you lose")
            running = False
        elif player == 3 and computer == 1:
            print(" you lose ")
            print(computer)
            running = False
        elif player == 4 and computer == 1:
            print(" you lose ")
            print(computer)
            running = False
        elif player == 3 and computer == 2:
            print("you lose")
            print(computer)
            running = False
        elif player == 4 and computer == 2:
            print("you lose")
            print(computer)
            running = False
        elif player == 5 and computer == 2:
            print("you lose")
            print(computer)
            running = False
        elif player == 4 and computer == 3:
            print(" you lose")
            print(computer)
            running = False
        elif player == 5 and computer == 3:
            print(" lose")
            print(computer)
            running = False
        elif player == 5 and computer == 3:
            print(" you lose")
            print(computer)
            running = False
        elif player == 2 and computer == 3:
            print("you lose")
            print(computer)
            running = False
        elif player == 2 and computer == 4:
            print(" you lose")
            print(computer)
            running = False
        elif player == 2 and computer == 4:
            print(" you lose ")
            print(computer)
            running = False
        elif player == 2 and computer == 5:
            print(" you lose ") 
            print(computer)
            running = False  
        elif player == 3 and computer == 4:
            print("you lose")
            print(computer)
            running = False
        elif player ==  3 and computer == 5:
            print(" you lose")
            print(computer)
            running = False
        elif player == 4 and computer == 5:
            print(" you lose ")
            print(computer)
            running = False
        elif player == 5 and computer == 4 or 3 or 2 or 1:
            print(" you lose")
            print(computer)
            running = False
        elif player == 4 or 3 or 2 or 1 and computer == 5:
            print(" you lose ")
            print(computer)
            running = False
        elif player ==  3 or 2 or 1 and computer == 4:
            print(" you lose")
            print(computer)
            running = False
        elif player == 2 or 1 and computer == 3:
            print(" you lose")
            print(computer)
            print("thanks for playing")
            running = False
        elif player == 1 and computer == 2:
            print(" you lose")
            print(computer)
            print("thanks for playing")
            running = False
        elif player == 5 and conmputer == 4 or 3 or 2 or 1:
            print(" you lose ")
            print(computer)
            print("thanks for playing")
            running = False
        elif player == 4 and computer == 3 or 2 or 1:
            print(" you lose ")
            print(computer)
            print("thanks for playing")
            running = False
        elif player == 3 and computer == 2 or 1:
            print(" you lose")
            print(computer)
            print("thanks for playing")
            running = False
        elif player == 2 and computer == 1:
            print(" you lose")
            print(computer)
            print("thanks for playing")
            running = False
else:
    if player == 'calculater':
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
    
elif player == 'dice':
    #dice







   options = ("move, investigate, run")
player = input("what doyou want to do?:")
if player == "run":
  roll = random.choice(" 1 2 3 4 5 6")
  print(roll)


    
else:
    if player == 'dugeon':
        # dugeon game
# game



     inventory = [" torch, apple, axe"]
room_has_key = True
has_won = False



print("---WELCOM TO THE DUGEON---")
print("Comands: 'look', 'grab', 'bag', 'unlock', 'quit'")


while not has_won :
    action = input("\ndo you want to do? ").lower().strip

    if action == "quit":
        print(" you gave up! game over")
        break


    elif action == "look":
        if room_has_key:
            print(" you are in a dark room. you see a shinny key and a locked door. ")
        else:
            print(" your in a dark room with a locked door at the end wall.")




    elif action == "grab":
        if room_has_key:
            inventory.append(" key")
            room_has_key == False
            print(" you grabed the key")
        else:
             print(" there is nothing to grab")


    elif action == "bag":
        print("---Your inventorry--")

        for item in inventory:
            print(f"-{item}")


    elif action == "ulock":
        if "key" in inventory:
            print( "you turn the key... and the door swings open  and you esape!" )
            has_won = True
        else:
            print("its locked")

    else:
        print("invalid command. 'bag', 'grab', 'unlock', or 'quit'")

print("Thanks for playing")








    




        
