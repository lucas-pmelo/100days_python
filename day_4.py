import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

choose = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

game = [rock, paper, scissors]

choose = game[choose]

computer_choose = random.randint(0, 2)

if choose == game[0] and computer_choose == 0:
    print(rock)
    result = "draw"
elif choose == game[1] and computer_choose == 1:
    print(paper)
    result = "draw"
elif choose == game[2] and computer_choose == 2:
    print(scissors)
    result = "draw"
elif choose == game[0] and computer_choose == 1:
    print(rock)
    result = "computer"
elif choose == game[0] and computer_choose == 2:
    print(rock)
    result = "player"
elif choose == game[1] and computer_choose == 0:
    print(paper)
    result = "player"
elif choose == game[1] and computer_choose == 2:
    print(paper)
    result = "computer"
elif choose == game[2] and computer_choose == 0:
    print(scissors)
    result = "computer"
elif choose == game[2] and computer_choose == 1:
    print(scissors)
    result = "player"

computer_choose = game[computer_choose]

print("\nComputer chooses:\n")
print(computer_choose)

if result == "draw":
    print("It was a draw!")
elif result == "player":
    print("You win!")
elif result == "computer":
    print("You lose!\n")
