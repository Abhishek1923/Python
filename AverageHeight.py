# You are going to write a program that calculates the average student height from a List of heights.
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


total_height = 0
for height in student_heights:
  total_height += height
# print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
# print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(average_height)
