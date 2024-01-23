import cv2

path = r'C:\Users\nikhi\OneDrive\Desktop\Project\Attendance Tracker\Students'
print("ADD NEW STUDENT\n")
F_name = input("Enter First Name: ")
L_name = input("Enter Last Name: ")
roll_no = input("Enter Roll Number: ")

final_name = roll_no + "_" + F_name + "_" + L_name
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        print('failed to grab frame')
        break
    cv2.imshow('test', frame)
    k = cv2.waitKey(1)
    # if the escape key is been pressed, the app will stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Q hit, closing the app')
        break
    elif k % 256 == 32:     # Press spacebar to take image
        cv2.imshow("IMAGE", frame)

        # saving image in local storage
        cv2.imwrite(fr'C:\Users\nikhi\OneDrive\Desktop\Project\Attendance Tracker\Students\{final_name}.jpeg', frame)
        print('screenshot taken')

# release the camera
cam.release()
# stops the camera window
