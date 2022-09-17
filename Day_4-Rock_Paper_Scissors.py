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

#Write your code below this line 👇
import random

options = [rock, paper, scissors]
player_choice_index = int(input("Welcome to Rock, Paper, Scissors!\nRemember that 0 is for Rock, 1 is for Paper, and 2 is for Scissors!\nWhat's your choice? "))

if player_choice_index >= 3 or player_choice_index < 0: print("\nYou typed an invalid number. You lose!\n")
else:
  player_choice = options[player_choice_index]
  
  print("\nYou chose:")
  print(player_choice)
  
  computer_choice_index = random.randint(0, 2)
  computer_choice = options[computer_choice_index]
  
  print("\nThe computer chose:")
  print(computer_choice)
  
  win = "You win!"
  lose = "You lose!"
  print()
  
  if player_choice == computer_choice: print("It's a tie!")
  
  elif player_choice == rock and computer_choice == paper: print(lose)
  elif player_choice == rock and computer_choice == scissors: print(win)
  
  elif player_choice == paper and computer_choice == rock: print(win)
  elif player_choice == paper and computer_choice == scissors: print(lose)
  
  elif player_choice == scissors and computer_choice == rock: print(lose)
  elif player_choice == scissors and computer_choice == paper: print(win)
