#Code1
#TODO 1:Ask user to choose random word from the word_list and assign it to a variable called chosen_word .then print it
import random

world_list=["Apple","Banana","Mango","Orange","Kiwi"]
chosen_world=random.choice(world_list)
print(chosen_world)

#TODO 2:Ask user to guess a letter and assign their answer to a variable called guess. make guess lowercase
guess=input("Guess a letter\n").lower()
print(guess)

#TODO 3:Check if the letter the user guessed(guess) is one of the letter in the chosen_word.Print "Right" if it is,"Wrong" if it's not.
for letter in chosen_world:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

#Code2
#TODO 1: Create empty string called placeholder
placeholder=" "
word_length=len(chosen_world)
for letter in range(word_length):
    placeholder += "_"
print(placeholder)

#TODO 2: Create Display the puts the guess letter in the right position and _ in the rest of the string
display=""
for letter in chosen_world:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
