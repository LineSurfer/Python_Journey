print("Python Pizza Delivery \n")

total_value = 0

size = input("Welcome to Python Pizza! What size of pizza do you want? Small, Medium, or Large? \n")

if size == "Small":
    print("You picked Small Pizza. That will be 15$.\n" )
    total_value += 15
elif size == "Medium":
    print("You picked Medium Pizza. That will be 20$.\n")
    total_value += 20
elif size == "Large":
    print("You picked large Pizza. That will be 25$.\n")
    total_value += 25
else:
    print("Sorry, we don't have that size yet.\n")


pepperoni = input("Do you want Pepperoni? Yes or No \n")

if pepperoni == "Yes":
    print("You added Pepperoni on your pizza. That will be additional 2$.\n")
    total_value += 2
else:
    print("You didn't add Pepperoni. Noted.")

cheese = input("Do you want extra cheese? Yes or No.\n")

if cheese == "Yes":
    if size == "Small" or "Medium":
        total_value += 3
    else:
        total_value += 5
else:
    print("You didn't add extra cheese. Noted.")

print("You will pay a total of " + str(total_value) + "$.\nThank you for choosing us. Enjoy your food!")