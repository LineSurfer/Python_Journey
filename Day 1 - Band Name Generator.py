# import time to use the typewriter delay effect
import time

# define typewriter effect to apply it to whole code
def typewriter_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


# while true to loop the code endlessly until "exit" is input by the user
while True:
    typewriter_print("Greetings! I am the greatest Band Name Generator.\n")

    time.sleep(0.3) 

    typewriter_print("\nCan I ask what is your first name?\n")
    first_name = input()
    if first_name == "exit":
        break

    time.sleep(0.3)  

    typewriter_print("\nGreat! Hello " + first_name +
                     "! That's a beautiful name.\n")

    time.sleep(0.3)  

    typewriter_print("\nIn what city did you grow up?\n")
    city_name = input()

    time.sleep(0.3)  

    typewriter_print(
        "\nWell, that's a fantastic city, isn't it? " + city_name + "!\n")

    band_name = first_name + " " + city_name + "!"
    typewriter_print("\nYour amazing band name will be " + band_name + "\n")

    time.sleep(0.3)  

    typewriter_print(
        "\nThanks for using Band Name Generator. Hope you liked it!\n\n")
