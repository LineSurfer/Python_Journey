print("Treasure Map - Where do you want to hide it? \n")

row1 = ["o", "o", "o"]
row2 = ["o", "o", "o"]
row3= ["o", "o", "o"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put the treasure? Column and Row\n")
#23
#first digit = column
#second digit = row
#put your code here

horizontal = int(position[0]) #row
vertical = int(position[1]) #column

selected_row = map[vertical -1 ]
selected_row[horizontal -1] = "X"






# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}\n")