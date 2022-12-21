# The rules of the game:
# The player should roll two dice. If the sum of both of them is 7 or 11 the player wins. If the sum is 2, 3 or 12 (craps) the casino wins. If during the first roll the sum is 4, 5, 6, 8, 9 or 10, that number becomes the “goal” number. To win, the player should roll the dice till they roll the goal number again. If the player rolls a 7 before rolling the goal number, they lose.
# Your task is to recreate this game using Python. Your program should roll two dice and output the sum of two random numbers. By following the rules of the game, your program should decide whether the player wins or loses.

import random
import time

PLAYER_WINS = [7, 11]
CASINO_WINS = [2, 3, 12]
result = None
goal_number = 0

print("Hi there, let's start the game. Roll the dices!")
time.sleep(2)  # added so that any feedback is printed out before the next prompt

def roll():
  """ The function generates two random integers for two dices per each roll. And returns the sum of two dices. """
  roll_1 = random.randint(1, 6)
  roll_2 = random.randint(1, 6)
  _sum = roll_1 + roll_2
  print(f"The sum of the roll is {_sum}.")
  time.sleep(2) 
  return _sum


output_1 = roll()  # we assign the sum of two dices from the FIRST roll is assigned to the variable output_1.

# next, the program checks on wheither the sum of the roll is from winning or losing lists

if output_1 in PLAYER_WINS:
  result = "Congratulations, You won!"
elif output_1 in CASINO_WINS:
  result = "Unfortunalty, You lost"
else:  # if the sum is 4, 5, 6, 8, 9 or 10, that number becomes the goal number.
  goal_number = output_1
  print(f"So far you neither win nor lost, now your goal number is {goal_number}. Roll the dices.")
  time.sleep(2) 
  # while loop will continue to execute a roll function as long as a the result variable hasn't changed its initial value.
  while result is None: 
    output = roll() 
    if output == 7:
      result = "Unfortunalty, You lost"
    elif output == goal_number:
      result = "Congratulations, You won!"

print(result)