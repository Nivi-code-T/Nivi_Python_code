import random

r1=random.randint(1,10)
print(r1)

r2=random.choice([0,1,2,3])
print(r2)

#random heads or tails
choice=random.randint(0,1)
if choice == 0:
    print("Heads")
else:
    print("Tails")

#Python List: Appending List
my_list=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland"]
print(my_list[0])
my_list.append("Texas")
print(my_list)
my_list[4]='New York'
print(my_list)

#Extend List
my_list.extend(["Virginia, Washington"])
print(my_list)

#Insert new value to the List
my_list.insert(0,'New York')
print(my_list)

#Remove Value from the list
my_list.remove('New York')
print(my_list)

#Remove Item using pop() will remove last item from the list
my_list.pop(1)
print(my_list)
