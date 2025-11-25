#Treasure haunt
print("Welcome to Treasure island\nyour mission is to find the treasure")
direction=input("You're at a cross road. Where do you want to go? Type left or right")
if direction == 'left':
     print("you've come to a lake. there is an island in the middle of the table")
     select=input("Type wait or swim?")
     if select == 'wait':
        print("you arrived at Island unharmed")
        colour=input("which colour do you choose?")
        if colour == 'Yellow':
          print("You win")
        elif colour == 'red':
          print("It;s room full of fire .Game Over")
        elif colour=='blue':
          print("You enter a room of beast. game Over")
        else:
         print("you choose door that doesn't exist. Game Over")
     else:
         print("you got attacked by an angry trout. game Over")
else:
       print("game over")

