import os
from known_face_encoding import list1

print("\nDELETE STUDENT\n")
roll_no = input("Enter Roll Number to delete: ")

for students in list1:
    if roll_no == students.split('_')[0]:
        print(students)
        os.remove(fr'.\Students\{students}')
        print("Student data deleted succesfully\n")


