# Input a Python list of student heights
student_heights = input("enter height:").split()
total_height=0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

  total_height=int(total_height)+(student_heights[n])

number_of_students=len(student_heights)
average_height=round((total_height)/(number_of_students))

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")