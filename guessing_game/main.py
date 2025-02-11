import random

num_to_guess = random.randint(1,100)
num_guesses = 0

def choose_difficulty ():
    global num_guesses
    difficulty = input('Choose difficulty. type EASY or HARD: ')
    if difficulty.lower() == 'easy':
        num_guesses += 10
    elif difficulty.lower() == 'hard':
        num_guesses += 5

    return num_guesses

def play() :
    choose_difficulty()
    game_over = False
    print(num_to_guess)
    global num_guesses
    print(f'You have {num_guesses} guesses remaining')
    while not game_over:
        if num_guesses == 0:
            game_over = True
            print('You have run out of guesses, you lost')
        else:
            guess = int(input('Please guess the number: '))
            if guess == num_to_guess:
                game_over = True
                print('You have won')

            elif guess > num_to_guess:
                num_guesses -= 1
                print(f'TOO HIGH, you have {num_guesses} guesses remaining')
            elif guess < num_to_guess:
                num_guesses -= 1
                print(f'TOO LOW, you have {num_guesses} guesses remaining')


play()