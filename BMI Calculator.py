print("BMI Calculator \n")

weight = float(input("What is your weight in kilograms? \n"))
height = float(input("What is your height in meters? \n"))

calc = weight / (height ** 2)
rcalc = round(calc)

print("Your BMI is " + str(rcalc) + ". \n")

if rcalc < 18.5:
    print("You are underweight. Eat more healthy foods!")
elif rcalc < 24.9:
    print("You are healthy. Keep living the healthy way!")
elif rcalc < 30:
    print("You are overweight. You have to eat healthy foods and proper diet!")
else:
    print("You are obese. Consult your dietician for a healthy diet and do exercise daily. \n Keep that body fats burning!")

