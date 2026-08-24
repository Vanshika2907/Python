'''
Write a Python program for a Number Guessing Game.
'''
def guess_number():
    import random
    number = random.randint(1, 10)
    attempts = 0
    print("Guess the number between 1 and 10.")
    
    while attempts < 3:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low, Try again.")
        elif guess > number:
            print("Too high, Try again.")
        else:
            print("Correct Guess!")
            break
    else:
        print("All attempts used. The number was:", number)
guess_number()