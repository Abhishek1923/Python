# You are going to write a program that calculates the highest score from a List of scores.
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

#     The highest score in the class is: x

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# Write your code below this row 👇
max_score = 0
for scores in student_scores:
    if scores > max_score:
        max_score = scores
    else:
        continue
print(f"The highest score in the class is: {max_score}")
