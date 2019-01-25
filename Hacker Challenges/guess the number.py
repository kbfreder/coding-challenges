import random    
secret_number = random.choice(range(0,101))
guess = -1
count = 0
while secret_number != guess and count < 10:
    guess = int(input('Enter your guess: '))
    if guess < secret_number:
        print("your guess is low", count)
    elif guess > secret_number:
        print("your guess is high", count)
    else:
        print("your guess right!")
    count += 1
    