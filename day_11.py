import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game():
    print(logo)
    user_hand = []
    dealer_hand = []

    for i in range(2):
        user_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))

    print(f"\nThis is the dealer's hand: [{dealer_hand[0]}, x]")
    print(f"This is your hand: {user_hand}")

    user_score = sum(user_hand)

    print(f"\nYour current score is: {user_score}")

    if user_score == 21:
        print("\nYou win!")
        return

    draw = input("\nDo you want to draw another card? Type 'y' or 'n': ")

    while draw == "y":
        user_hand.append(random.choice(cards))
        print(f"\nThis is your hand: {user_hand}")
        user_score = sum(user_hand)
        print(f"Your current score is: {user_score}")
        if user_score > 21:
            print("\nYou lose!")
            return

        draw = input("\nDo you want to draw another card? Type 'y' or 'n': ")

    dealer_score = sum(dealer_hand)

    while dealer_score < 17:
        dealer_hand.append(random.choice(cards))
        dealer_score = sum(dealer_hand)

    print(f"\nThis is the dealer's hand: {dealer_hand}")
    print(f"This is your hand: {user_hand}")
    print(f"\nYour current score is: {user_score}")
    print(f"The dealer's current score is: {dealer_score}")

    if dealer_score > 21:
        print("\nYou win!")
        return

    if user_score > dealer_score:
        print("\nYou win!")
        return
    else:
        print("\nYou lose!")
        return


game()
