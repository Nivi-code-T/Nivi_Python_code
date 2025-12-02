#for loop
fruits=['apple','banana','kiwi','orange']
for fruit in fruits:
    print(fruit)

#sum operation
score=[10,20,30,40,50,60,70,80,90,100]
print(f"Sum of score is {sum(score)}")

#how the sum operation works behind
sum=0
for i in score:
    sum+=i
print(f"Sum of score is {sum}")

#find max student score
max_score=[150,180,190,200,250,270,280,290]
print(f"Max Score {max(max_score)}")

#how max works behind
max=0
for score in max_score:
        if score > max :
            max = score
            print(max)
print(f"Max1 Score {max}")

#for loop with range function
sum=0
for number in range(1,101):
    sum+=number
print(f"total: {sum}")

#FizzBuzz game
for number in range(1,101):
    if number % 3== 0 and number %5==0:
        print("FizzBuzz")

    elif number %3 == 0:
        print("Fizz")

    elif number % 5==0:
        print("Buzz")

    else:
        print(number)
