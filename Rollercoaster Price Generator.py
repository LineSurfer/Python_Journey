print("Rollercoaster Ride Price Generator \n")

height = int(input("What is your height in cm? \n"))

ticket = 0

if height > 120:
    age = int(input("What is your age? \n"))
    if age < 12:
        ticket += 5
        print("Child ticket price is 5$.\n")
    elif age < 18:
        ticket += 7
        print("Teenager ticket price is 7$.\n")
    elif age >= 48 and age <= 55:
        ticket += 0
        print("Your ticket is free. Enjoy the ride!")
    else:
        ticket += 12
        print("Adult ticket price is 12$.\n")

    photos = input("Do you want photos to be taken during your ride?\n Yes or No \n")

    if photos == "Yes":
        ticket += 3
        print("Your total ticket price is " + str(ticket) + "$.\n\nSmile and Enjoy your ride!")
    else:
        print("That's fine. Your total ticket price is " + str(ticket) + "$.\n\nEnjoy the ride!")
else:
    print("Sorry, you are not tall enough for this ride today.\n You can try other rides! :)")