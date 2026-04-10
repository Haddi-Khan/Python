# 17.	Guess the Number Game – Random number guessing with hints.
secret = 60
while True:
    guess= int(input("Enter any number between 1 to 100: "))
    if guess == secret:
            print("your answer is right")
            break
    elif guess < secret:
        print("your answer is low")
    else:
        print("your answer is high")
