list_of_students = []

while True:
    first_name = input("Enter the student first name: ")
    last_name = input("Enter the student last name: ")
    matric_number = input("Enter the student number: ")
    student_details = {}
    student_details["first_name"] = first_name
    student_details["last_name"] = last_name
    student_details["matric_number"] = matric_number
    list_of_students.append(student_details)
    
    add_new_student = int(input("""Do you want to exit or add a new student:
                                1 for yes. 
                                0 for exist: 
"""))
    if not add_new_student:
      break

print("Printing the students details".center(50, "*"))
for student in list_of_students:
    print(f"{student["first_name"]} with matric number f{student["matric_number"]}, come forward.")
    
    