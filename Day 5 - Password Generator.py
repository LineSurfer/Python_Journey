import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
number_letters= int(input("How many letters would you like in your password?\n"))
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
#Easy Level
#Easy Level

# gletter = ""
# for i in range (0,number_letters):
#     random_letters = random.randint(0,51)
#     generated_letters = letters[random_letters]
#     gletter += generated_letters
#
# gnumber = ""
# for i in range (0,number_numbers):
#     random_number = random.randint(0,9)
#     generated_number = numbers[random_number]
#     gnumber += generated_number
#
# gsymbol = ""
# for i in range (0,number_symbols):
#     random_symbols = random.randint(0,8)
#     generated_symbols = symbols[random_symbols]
#     gsymbol += generated_symbols
#
# total_characters = number_letters + number_numbers + number_symbols
# gpassword = (gletter + str(gnumber) + str(gsymbol))
#
# print("Your generated password is " +str(gpassword))

#Hard level
#Hard level
#Hard level

password = []

for char in range (1, number_letters + 1):
    password.append(random.choice(letters))

for char in range (1, number_numbers + 1):
    password.append(random.choice(numbers))

for char in range (1, number_symbols + 1):
    password.append(random.choice(symbols))

random.shuffle(password)

spassword = ""

for char in password:
    spassword += char

total_characters = number_numbers + number_letters + number_symbols
print(f"Your generated password is: {spassword}.\n")
print("Your password's total character is " + str(total_characters) + ".")