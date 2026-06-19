students_list = []
def add_student():

    while True:
       student_name = input("Enter the student's name (or 'exit' to quit): ")
       if student_name.lower() == 'exit':
        break
    
       student_grade = float(input("Enter the student's grade: "))
       if student_grade < 0 or student_grade > 100:
        raise ValueError("Grade must be between 0 and 100."+"And you entered: "+str(student_grade))
        continue

       student = dict()
       student_id = len(students_list) + 1
       student['id'] = student_id
       student['name'] = student_name
       student['grade'] = student_grade
       students_list.append(student)


