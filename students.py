from datetime import date, datetime

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
       def determine_letter_grade(grade):
        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        elif grade >= 50:
            return 'E'
        elif grade >= 40:
            return 'S'
        else:
            return 'F'
       today = datetime.now().strftime("%Y%m%d")

        # Count students created today
       count = sum(student["id"].startswith(today) for student in students_list) + 1

        
 
       student = dict()
       student_id = f"{today}-{count}"
       student['id'] = student_id
       student['name'] = student_name
       student['grade'] = student_grade
       student["letter_grade"] = determine_letter_grade(student_grade)
       student["status"]= "Active"
       student["letter_grade"]
       students_list.append(student)

def save_students():

    with open("data.txt", "w") as file:

        for student in students_list:

         file.write(
    f"{student['id']},{student['name']},{student['grade']},{student['letter_grade']},{student['status']}\n"
)
def load_students():
    students_list.clear()
    try:

        with open("data.txt", "r") as file:

            for line in file:

                student_id, name, grade, letter_grade, status = line.strip().split(",")

                students_list.append({
                    "id": int(student_id),
                    "name": name,
                    "grade": float(grade),
                    "letter_grade": letter_grade,
                    "status": status
                })

    except FileNotFoundError:
        pass


