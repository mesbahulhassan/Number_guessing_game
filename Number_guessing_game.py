import random
low = int(input('input the lower value of the game you want to play: '))
high = int(input('input the higher value of the game you want to play: '))
num = random.randint(low, high)
guesses = int(input("enter the number of guesses you want to have: "))
while guesses > (high - low):
    print(f"guesses must be equal to or less than {high - low}")
    guesses = int(input("enter the number of guesses you want to have: "))

while guesses > 0:
    try:
        guess = int(input(f'Guess a number from {low} to {high}: '))
        while guess > high or guess < low:
            print(f'Your guess is out of range {low} and {high}')
            guess = int(input(f'Guess a number from {low} to {high}: '))

        if guess > num:
            guesses -= 1
            print(f"Guess Lower\nRemaining attempt {guesses}")

        elif guess < num:
            guesses -= 1
            print(f"Guess Higher\nRemaining attempt {guesses}")

        else:
            print("You guessed correctly")
            break

    except ValueError:
        print("Value Error --> Enter a real Integer from this range")

print('Game Ended')









