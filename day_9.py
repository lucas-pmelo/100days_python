import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Welcome to the secret auction program.")
bids = {}
stop = False


def find_winner(bids):
    name_higher = ""
    higher = 0
    for name in bids:
        if int(bids[name]) > higher:
            higher = int(bids[name])
            name_higher = name

    print(f"The winner is {name_higher} with a bid of ${higher}")


while not stop:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bids[name] = bid

    more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more == 'no':
        stop = True
    clear()

find_winner(bids)
