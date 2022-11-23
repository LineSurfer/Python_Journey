import random

print("Heads or Tails \n")

random_number = random.randint(1,100)
if random_number >= 50:
    print("Heads")
else:
    print("Tails")

print(random_number)