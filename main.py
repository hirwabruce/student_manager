from students import*
load_students()
print("Student Management System")
action = input("Enter 'add' to add a student or 'view' to view students: ")

if action.lower() == 'add':
    from students import add_student
    add_student()
    save_students()
elif action.lower() == 'view':
    from viewstudents import view_students
    view_students()