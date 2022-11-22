print("Love Calculator \n")

name1 = input("Input your name: \n")
name2 = input("Input the other name: \n")

combined_name = name1 + name2
lower_string = combined_name.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")
true = t + r + u + e
strue = str(true)
l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")
love = l + o + v + e
slove = str(love)

love_score = strue + slove
ilove_score = int(love_score)
if ilove_score < 10 or ilove_score > 90:
    print("Your score is " + str(love_score) + " , you go together like coke and mentos.")
elif ilove_score > 40 and ilove_score < 50:
    print("Your score is " + str(love_score) + " , you are alright together.")
else:
    print("Your score is " + str(love_score) + ".")


# name1 = name1.lower()
# name2 = name2.lower()
#
# whole_name = name1 + name2
# print(whole_name)

# t = (name1.lower().count("t"))
# r = (name1.lower().count("r"))
# u = (name1.lower().count("u"))
# e = (name1.lower().count("e"))
#
# true_total = int(t) + int(r) + int(u) + int(e)
# print("T occurs " + str(t) + " times.")
# print("R occurs " + str(r) + " times.")
# print("U occurs " + str(u) + " times.")
# print("E occurs " + str(e) + " times.\n")
# print("Total: " + str(true_total) +"\n")
#
# l = (name2.lower().count("l"))
# o = (name2.lower().count("o"))
# v = (name2.lower().count("v"))
# ee = (name2.lower().count("e"))
#
# print("L occurs " + str(l) + " times.")
# print("O occurs " + str(o) + " times.")
# print("V occurs " + str(v) + " times.")
# print("E occurs " + str(ee) + " times.\n")
#
# love_total = int(l) + int(o) + int(v) + int(ee)
# print("Total: " + str(love_total) + "\n")








