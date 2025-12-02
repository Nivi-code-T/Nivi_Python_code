# #Pypassword generator
import random
import string
#letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letters=string.ascii_uppercase + string.ascii_lowercase
numbers=['0','1','2','3','5','6','7','8','9']
symbols=['!','#','$','%','^','&','*','(',')','_']
print("Welcome to the PyPassword Generator!")
l_letters=int(input("How many Letters would you like in your password\n"))
s_symbol=int(input("How many symbols would you like?\n"))
n_number=int(input("How many numbers would you like?\n"))
password_list=[]
for char in range(0,l_letters):
       password_list.append(random.choice(letters))

for number in range(0,n_number):
       password_list.append(random.choice(numbers))

for symbol in range(0,s_symbol):
    password_list.append(random.choice(symbols))

#print(password_list)
random.shuffle(password_list)
#print(password_list)
password=""
for char in password_list:
    password +=char
print(password)

#OR using different methods
letters=string.ascii_uppercase + string.ascii_lowercase
numbers=['0','1','2','3','5','6','7','8','9']
symbols=['!','#','$','%','^','&','*','(',')','_']
print("Welcome to the PyPassword Generator!")
l_letters=int(input("How many Letters would you like in your password\n"))
s_symbol=int(input("How many symbols would you like?\n"))
n_number=int(input("How many numbers would you like?\n"))
password=""
for char in range(0,l_letters):
    password +=random.choice(letters)

for number in range(0,n_number):
    password += random.choice(numbers)

for symbol in range(0,s_symbol):
    password += random.choice(symbols)

print(password)
password_list=list(password)
print(password_list)
random.shuffle(password_list)
print("".join(password_list))











