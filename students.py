students_list = []
def add_student():

    while True:
       student_name = input("Enter the student's name (or 'exit' to quit): ")
       if student_name.lower() == 'exit':
        break
    
       student_grade = float(input("Enter the student's grade: "))
       if student_grade < 0 or student_grade > 100:
         print("Grade must be between 0 and 100.")
         continue

       student = dict()
       student_id = len(students_list) + 1
       student['id'] = student_id
       student['name'] = student_name
       student['grade'] = student_grade
       students_list.append(student)

def save_students():

    with open("data.txt", "w") as file:

        for student in students_list:

         file.write(
    f"{student['id']},{student['name']},{student['grade']}\n"
)
def load_students():
    students_list.clear()
    try:

        with open("data.txt", "r") as file:

            for line in file:

                student_id, name, grade = line.strip().split(",")

                students_list.append({
                    "id": int(student_id),
                    "name": name,
                    "grade": float(grade)
                })

    except FileNotFoundError:
        pass


