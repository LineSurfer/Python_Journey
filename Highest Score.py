student_scores = input("Input the list of student scores: \n").split()
# student_heights.sort()
for i in range (0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
# # 78 65 89 86 55 91 64 89
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}.")
