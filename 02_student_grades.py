students = {
    "Rahul": "A",
    "Priya": "B",
    "Arjun": "C"
}

while True:
    print("    Student Grades    ")
    print("1. Add a new student")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists.")
        else:
            grade = input("Enter grade: ").upper()
            students[name] = grade
            print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name to update: ")

        if name in students:
            grade = input("Enter new grade: ").upper()
            students[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("All Student Grades:")

        for name, grade in students.items():
           print(name, ":", grade)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")