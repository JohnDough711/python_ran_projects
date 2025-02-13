import random
from game_data import data

def format_data(account):
    acc_name = account['name']
    acc_description = account['description']
    acc_country = account['country']

    return f'{acc_name}, a {acc_description} from {acc_country}'


#need to check if the answer is correct
def check_if_correct(guess, a_followers, b_followers):
    user_guess = guess.lower()
    if a_followers > b_followers:
        return user_guess == "a"
    elif a_followers < b_followers:
        return user_guess == 'b'

game_should_continue = True
score = 0
#generate random account
acc_b = random.choice(data)

while game_should_continue:
    acc_a = acc_b
    acc_b = random.choice(data)

    #handle if acc_b and acc_b are same
    if acc_a == acc_b:
        acc_b = random.choice(data)

    print(f'Compare {format_data(acc_a)}')
    print('VS')
    print(format_data(acc_b))

    #ask user for an input
    while True:
        try:
            u_guess = input('Please guess which has higher follower count, either a or b: ')
            if u_guess.isdigit():
                raise ValueError("Input should be a letter a or b")
            elif u_guess != 'a' and u_guess != 'b':
                raise ValueError("Input should be a letter a or b")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


    #check if the answer is correct and add to score
    is_correct = check_if_correct(u_guess, acc_a['follower_count'], acc_b['follower_count'])

    if is_correct:
        score += 1
        print(f"You have guessed correctly, current score: {score}")
    elif not is_correct:
        game_should_continue = False
        print('You have guessed incorrectly, GAME OVER')
