#Task 1: Create a Dictionary of Student Marks
# Creates a dictionary where student names are keys and their marks are values.
student_marks = {'Alice':85,'sia':65,'tom':90,'mike':45}
# Retrieves and displays the corresponding marks.
# If the student’s name is not found, display an appropriate message.
name = input("enter the name of the student:")
if name in student_marks.keys():
    print(name+"'s marks is :",student_marks[name])
else:
    print("student name not found")
