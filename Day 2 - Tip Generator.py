print("Tip Generator \n")

total_value = float(input("Enter the total value: $\n"))

tip_percent = float(input("How much percentage do you want to tip? \n"))

total_person = int(input("How many of you are going to share? \n"))

total = (total_value + (tip_percent / 100)) / total_person

rounded_total = round(total, 2)

print("Each person will pay " + str(rounded_total) + "$ equally for the tip.")