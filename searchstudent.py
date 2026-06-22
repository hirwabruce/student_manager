from students import students_list

def search_student(name):
    for student in students_list:
        if student['name'].lower() == name.lower():
            print(f"ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")
            return student
        

    return None

