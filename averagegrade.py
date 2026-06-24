from students import students_list
def calculate_average_grade():
    
    if not students_list:
        print("No students found.")
        return

    total_grade = sum(student['grade'] for student in students_list)
    average_grade = total_grade / len(students_list)

    print(f"The average grade of all students is: {average_grade:.2f}")