import random
#ASCI ARTS
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#variables
rak = "Rock!"
peper = "Paper!"
sisor = "Scissor!"
#nested lists
game_images = [Rock, Paper, Scissor]
choices = [rak, peper, sisor]
#player choice
player_selection = int(input("What do you choose?\n0 for Rock\n1 for Paper\n2 for Scissor\n"))
print("You chose " + choices[player_selection] + game_images[player_selection])
#computer generated choice
computer_selection = random.randint(0,2)
print("Computer chose " + choices[computer_selection] + game_images[computer_selection])
#bunch of if else statements
if player_selection == 0 and computer_selection == 2:
    print("You win!")
elif player_selection == 0 and computer_selection == 1:
    print("You lose!")
elif player_selection == 0 and computer_selection == 0:
    print("It's a draw!")
elif player_selection == 1 and computer_selection == 0:
    print("You win!")
elif player_selection == 1 and computer_selection == 2:
    print("You lose!")
elif player_selection == 1 and computer_selection == 1:
    print("It's a draw!")
elif player_selection == 2 and computer_selection == 1:
    print("You win!")
elif player_selection == 2 and computer_selection == 0:
    print("You lose!")
elif player_selection == 2 and computer_selection == 2:
    print("It's a draw!")
else:
    print("You typed an invalid number. You lose!")