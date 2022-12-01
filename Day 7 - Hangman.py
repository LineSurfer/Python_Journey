import random

print("Play Hangman! \n")

word_list = ["jollibee", "chowking", "mang inasal"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
guess = input("Guess a letter: \n")

display = []
for letter in chosen_word:
    display += "_"

for position in range (word_length):
    letter = chosen_word[position]
    if guess == letter:
        display[position] = letter
print(display)

saved_display = []
for letters in display:
    saved_display += letters
print(f"Total letters guessed: {saved_display}" + ".")