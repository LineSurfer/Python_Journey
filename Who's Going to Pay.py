import random

print("Who's going to pay? \n")

names_string = input("List all the names separated by commas. \n ")
names = names_string.split(", ")

names_list = len(names)

going_to_pay = random.randint(0,names_list -1)

print(names[going_to_pay] + " is the lucky one who's going to pay everything.\nEnjoy the meal, lads!")
