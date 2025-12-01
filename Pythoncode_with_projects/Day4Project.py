import random
from turtledemo.nim import computerzug

game_image=['rock','paper','Scissor']
user_choice=int(input("what do you choose ? Type0 for rock, 1 for peper or 2 for scissor.\n"))
if user_choice >=0 and user_choice <=2:
    print(game_image[user_choice])
computer_choice = random.randint(0, 2)
print("computer chose:")
print(game_image[computer_choice])

if user_choice >=3 or user_choice < 0:
   print("you Entered Invalid number . you lose !")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif user_choice == 2 and computer_choice == 0:
    print("you lose")
elif user_choice == computer_choice:
    print("it's a draw!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
else:
    print("Invalid")




