from students import students_list, save_students

def delete_student(student_name):
    for student in students_list:

        if student["name"].lower() == student_name.lower():
            students_list.remove(student)
            save_students()  # Save changes to data.txt
            print(f"Student '{student_name}' deleted successfully.")
            return

    print(f"Student '{student_name}' not found.")