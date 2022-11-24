print("Treasure Map Placement Generator\n")
#rows are nested within map
row1 = ["X", "X", "X", "X", "X"]
row2 = ["X", "X", "X", "X", "X"]
row3 = ["X", "X", "X", "X", "X"]
row4 = ["X", "X", "X", "X", "X"]
row5 = ["X", "X", "X", "X", "X"]

map = [row1, row2, row3, row4, row5]

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")

print("Where do you want to put your treasure? \n")
#separated row and column selection to avoid confusion
row = int(input("Column (Vertical): \n"))
column = int(input("Row (Horizontal): \n"))

map[column - 1][row - 1] = "O"
#much easier to understand rather than this code
# selected_column = map[column - 1]
# selected_column[row - 1] = "O"

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")




