from students import students_list

def view_students():
   
    if not students_list:
        print("No students found.")
        return

    print("List of Students:")
    for student in students_list:
        print(
            #f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Grade: {student['grade']}"
        )