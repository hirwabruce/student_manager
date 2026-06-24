from students import*
load_students()
print("Student Management System")
print("Student Management System Menu:")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Calculate Average Grade")
print("7. Exit")


action = input("Enter your choice number (add/view/search/update/delete/average/exit): ")

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
elif action.lower() == "delete" or action == "5":
    from deletestudent import delete_student
    student_name = input("Enter the student's name to delete: ")
    delete_student(student_name)
elif action.lower() == "average" or action == "6":
    from averagegrade import calculate_average_grade
    calculate_average_grade()
    

elif action.lower() == "exit" or action == "7":
    print("Exiting the program.")
    exit()