# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total = 0
number_of_students = 0
for i in range(len(student_heights)):
  total += student_heights[i]
  number_of_students = i 


print(f"total height = {total}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(total/len(student_heights))}")