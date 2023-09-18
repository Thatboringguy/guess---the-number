import random

n = random.randint(1,100)
start_count = 1 
guess_chances = 10 

while 1 <= guess_chances:
    num = int(eval(input("guess the number : ")))
    if num > n :
         print("your guess was too high",num)
    elif num < n :
         print("your guess was too low", num)

    else :
         print("you win")
         print(start_count, "number of guesse you took")

    guess_chances -= 1
    print(guess_chances, "guesses left")
    start_count += 1
    print()

print("game over")
print("number is", n)