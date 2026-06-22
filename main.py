from students import*
load_students()
print("Student Management System")
print("Student Management System Menu:")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Update Student")

action = input("Enter your choice number (add/view/search/update): ")

if action.lower() == "add" or action == "1":
    from students import add_student
    add_student()
    save_students()
elif action.lower() == "view" or action == "2":
    from viewstudents import view_students
    view_students()
elif action.lower() == "search" or action == "3":
    from searchstudent import search_student
    name = input("Search name: ")
    student = search_student(name)

    if student:
      print(student)
    else:
      print("Student not found")
elif action.lower() == "update" or action == "4":
    from updategrade import update_grade
    name = input("Enter the student's name to update: ")
    new_grade = float(input("Enter the new grade: "))
    update_grade(name, new_grade)
