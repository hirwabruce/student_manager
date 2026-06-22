from students import load_students, save_students, students_list
def update_grade(student_name, new_grade):
    for student in students_list:
        if student["name"] == student_name:
            student["grade"] = new_grade
            save_students()  # Save changes to data.txt
            print("Grade updated successfully.")
            return

    print("Student not found.")

