import face_recognition
import os

list1 = os.listdir(r'C:\Users\nikhi\OneDrive\Desktop\Project\Attendance Tracker\Students')
list2 = []
dict1 = {}
for li in list1:
    li = li.split('.')[0]
    key = li.split('_')[0]
    value = li.split('_')[1] + " " + li.split('_')[2]
    dict1[key] = value
    list2.append(value)

test_image = []
known_face_encoding = []
test_encoding = []
for i in range(0, len(list1)):
    test_image.append(face_recognition.load_image_file
                      (fr"C:\Users\nikhi\OneDrive\Desktop\Project\Attendance Tracker\Students\{list1[i]}"))
    test_encoding = face_recognition.face_encodings(test_image[i])[0]
    known_face_encoding.append(test_encoding)
known_face_names = list2
students = known_face_names.copy()

