import random

def deal_card ():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return 'Draw'
    if u_score == 0:
        return 'You win with a blackjack'
    if c_score == 0:
        return 'Lose opponent has a black jack'
    if u_score > 21:
        return 'You went over. Opponent wins'
    if c_score > 21:
        return 'Opponent went over. You win'
    if u_score > c_score:
        return "You win"
    else:
        return "Computer wins"



def play_game():
    user_cards = []
    computer_cards = []
    game_over = False
    user_score = -1
    computer_score = -1

    for cards in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your Cards: {user_cards}, Your Current Score: {user_score}')
        print(f'Opponent Cards: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_hits = input('type y to get one more card, type n to pass')
            if user_hits == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score <= 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Your Final hand: {user_cards}. Your final score: {user_score}')
    print(f'Opponents Final hand: {computer_cards}. Opponents final score: {computer_score}')
    print(compare(u_score = user_score, c_score = computer_score))

while input('Do you wish to play a game of BlackJack? type y or n:') == 'y':
    print("\n" * 20)
    play_game()