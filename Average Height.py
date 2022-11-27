student_heights = input("Input the list of student heights: \n").split()
student_heights.sort()
for i in range (0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

print("Ascending order of height from taller to smaller: \n" + str(student_heights))

total_height = 0
for height in student_heights:
    total_height += height
print("The total height of students is " + str(total_height) + ".")

number_of_students = 0
for n_of_students in student_heights:
    number_of_students += 1
print("The total number of students is " + str(number_of_students) + ".")

average_height = round(total_height / number_of_students)

print("The average height of students is " + str(average_height) + ".")

#total height
#total number of students
#average height