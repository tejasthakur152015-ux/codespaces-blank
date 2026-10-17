# nasa intreview
# fuction and if else loops practice!



def greet(last_name, first_name):
    print(f" Hi{last_name} {first_name}")
    print("lets see your collage applicatiion")


greet( "Tejas", "Thakur" )

name = input("Enter your name")
age = int(input("Enter your age:"))
gpa = int(input("Enter your gpa:"))

if age >= 18 and gpa >= 3:
   print("nice now we will ask you two questions and then discuse if to hire you or not.")
   question_1 = ("how far away is jupiter from earth?")
   options = ("444000000000 , 314000000000, 932000000, or 56200000?")
   print(options)
   player = int(input("Enter a choice:"))
if player == 444000000000:
    print("correct!")
    question_2 = (" 999 * 999")
    options = ("998001, 890012, 999991,99890")
    print(options)
    player = int(input("Enter a choice"))
if player == 998001:
    print("correct")
    print(" congratts your the new ceo of nasa!")

    breakpoint
    
elif player == 999991:
    print("wrong")
elif player == 890012:
    print("wrong")
elif player == 99890:
    print("wrong")
elif player == 932000000000:
    print("wrong")
elif player == 562000000000:
    print("wrong")
elif player == 314000000000:
    print("wrong")
else:
    print("sorry but your not eligible")
    




