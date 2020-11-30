# Day 4 of 100 - 100 Days of Code - The Complete Python Pro Bootcamp for 2021

# Random numbers

import random

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")

# Lists

# favoriteFoods = ["Bacon", "Rice", "Grapes", "Tomatoes", "French Fries", "Salmon"]
# print(favoriteFoods[2])
# # docs.python.org and search for data structures for more list methods
# favoriteFoods.append("Cake")
# favoriteFoods.extend(["Guacamole", "Pickle Juice"])

# print("Lunch roulette")
# nameAsCSV = input("Give me everybody's name, separated by a comma.\n")
# names = nameAsCSV.split(", ")
# print(random.choice(names) + " is going to buy the meal today.")

# Nested Lists
# veggies = ["Spinach", "Kale", "Celery", "Potatoes"]
# fruits = ["Strawberries",  "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",  "Pears", "Tomatoes"]
# dirtyDozen = [fruits, veggies]
# print(dirtyDozen)

# Treasure Map Exercise
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print("    1     2    3")
# print(f"1 {row1}\n2 {row2}\n3 {row3}")
# position = input("Where do you want to put the treasure? \n")
# # column first, then row
# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical - 1][horizontal - 1] = "🤑"
# print(f"{row1}\n{row2}\n{row3}")


print("Rock, Paper, Scissors Game")
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
player = input("Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
playerChoice = int(player)
if playerChoice == 0:
    print(rock)
elif playerChoice == 1:
    print(paper)
else:
    print(scissors)

computer = random.randint(0, 2)
print("Computer chose: ")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)
# Rock beats scissors, scissors beats paper, paper beats rock
if playerChoice == computer:
    print("It's a tie")
elif playerChoice == 0 and computer == 2 or playerChoice == 1 and computer == 0 or playerChoice == 2 and computer == 1:
    print("You win!")
else:
    print("You lose")