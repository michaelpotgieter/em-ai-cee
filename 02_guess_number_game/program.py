import random

print('----------------------------------')
print('|         GUESS THE NUMBER       |')
print('----------------------------------')
print()

# initialise numbers and ask for name
unumber_a = 0
unumber_b = 0
user_name = input('What is your name ')

print("I'll guess a number between two which you choose")
print()

# enforce two different numbers
while unumber_a == unumber_b:
    # Accept number from user and convert to integer
    unumber_a_text = input('Enter the first  number ')
    unumber_a = int(unumber_a_text)
    unumber_b_text = input('Enter the second number ')
    unumber_b = int(unumber_b_text)

    if unumber_a < unumber_b:
        number = random.randint(unumber_a, unumber_b)
        guess = unumber_a - 1
    elif unumber_a > unumber_b:
        number = random.randint(unumber_b, unumber_a)
        guess = unumber_b - 1
    else:
        print('You have entered the same number. Please select two different numbers.')
        print()

while guess != number:
    guess_string = input('What is your guess ')
    guess = int(guess_string)

    if guess < number:
        print('Sorry {}, your guess of {} is too LOW'.format(user_name, guess))
        print()
    elif guess > number:
        print('Sorry {}, your guess of {} is too HIGH'.format(user_name, guess))
        print()
    else:
        print('Well done {}, your guess of {} is CORRECT'.format(user_name, guess))
        print()
