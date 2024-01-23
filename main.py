def new_student():
    import new_student


def del_student():
    import del_student


def check_attendance():
    import check_attendance


run = False
while not run:
    print("STUDENT ATTENDANCE TRACKER\n")
    select = int(input("Enter number for required function:\n1.Begin Attendance Tracking\n2.Enter New Student "
                       "Data\n3.Delete Student Data\n4.Exit\n\nEnter: "))

    match select:
        case 1:
            check_attendance()
        case 2:
            new_student()
        case 3:
            del_student()
        case 4:
            run = True
            exit()
