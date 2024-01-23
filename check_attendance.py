import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import known_face_encoding as kn

video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

students = kn.known_face_names.copy()
face_locations = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date + '.csv', 'w+', newline='')
lnwriter = csv.writer(f)

def find_key(my_dict, svalue):
    for key, value in my_dict.items():
        if value == svalue:
            return key
    return None

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(kn.known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(kn.known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = kn.known_face_names[best_match_index]
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(gray, 1.1, 4)
                y1, x2, y2, x1 = face_locations[0]
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame,name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),2)

            face_names.append(name)
            if name in kn.known_face_names:
                if name in students:
                    students.remove(name)
                    roll_no = find_key(kn.dict1, name)
                    print(students)
                    current_time = now.strftime("%H:%M:%S")
                    lnwriter.writerow([roll_no, name, current_time])

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) & 0xFF ==  ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
