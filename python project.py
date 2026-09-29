students = {}
# Grade calculation
def grade(p):
    if p >= 90: return "A+"
    if p >= 80: return "A"
    if p >= 70: return "B+"
    if p >= 60: return "B"
    if p >= 50: return "C"
    if p >= 40: return "D"
    return "F"
# Attendance calculation
def attendance(total, attended):
    # avoid division by zero
    return (attended / total * 100) if total else 0
# Add a new student
def add_student():
    roll = input("Roll Number: ")

    # quick check for duplicates
    if roll in students:
        print("Student already exists!")
        return

    students[roll] = {
        "name": input("Name: "),
        "branch": input("Branch: "),
        "semester": input("Semester: "),
        "subjects": {},
        "total": 0,
        "attended": 0
    }

    print("Student added!")
# Add marks for subjects
def add_marks():
    roll = input("Roll Number: ")

    if roll not in students:
        print("Student not found!")
        return

    n = int(input("Number of subjects: "))
    subjects = {}

    # loop through subjects
    for i in range(n):
        subject = input(f"Subject {i + 1}: ")

        while True:
            try:
                marks = float(input("Marks (0-100): "))
                if 0 <= marks <= 100:
                    subjects[subject] = marks
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Enter a valid number.")

    students[roll]["subjects"] = subjects
    print("Marks added!")

# Add attendance details
def add_attendance():
    roll = input("Roll Number: ")

    if roll not in students:
        print("Student not found!")
        return

    try:
        total = int(input("Total classes: "))
        attended = int(input("Classes attended: "))

        # validation
        if total < 0 or attended < 0 or attended > total:
            print("Invalid attendance!")
            return

        students[roll]["total"] = total
        students[roll]["attended"] = attended

        print(f"Attendance: {attendance(total, attended):.2f}%")

    except ValueError:
        print("Enter valid numbers.")

# Generate student report
def student_report():
    roll = input("Roll Number: ")

    if roll not in students:
        print("Student not found!")
        return

    s = students[roll]

    print("\nSTUDENT REPORT")
    print("==============")
    print("Name:", s["name"])
    print("Roll No.:", roll)
    print("Branch:", s["branch"])
    print("Semester:", s["semester"])

    if not s["subjects"]:
        print("No marks available.")
        return

    subjects = s["subjects"]
    total = sum(subjects.values())
    percentage = total / len(subjects)
    att = attendance(s["total"], s["attended"])

    # show marks
    for subject, marks in subjects.items():
        print(f"{subject}: {marks:.2f}")

    print("Total:", f"{total:.2f}")
    print("Average:", f"{percentage:.2f}%")
    print("Grade:", grade(percentage))
    print("Attendance:", f"{att:.2f}%")
    print("Attendance Status:", "Good" if att >= 75 else "Warning")
    print("Best Subject:", max(subjects, key=subjects.get))
    print("Weakest Subject:", min(subjects, key=subjects.get))

    # performance summary
    if percentage >= 75:
        performance = "Excellent"
    elif percentage >= 60:
        performance = "Good"
    elif percentage >= 50:
        performance = "Average"
    elif percentage >= 40:
        performance = "Needs Improvement"
    else:
        performance = "Poor"

    print("Performance:", performance)

# Display all students
def display_students():
    if not students:
        print("No students registered.")
        return

    print("\nALL STUDENTS")
    print("============")
    for roll, s in students.items():
        print(roll, "-", s["name"], "-", s["branch"])

# Performance analysis for class
def performance_analysis():
    data = []

    for roll, s in students.items():
        if s["subjects"]:
            p = sum(s["subjects"].values()) / len(s["subjects"])
            data.append((roll, s["name"], p))

    if not data:
        print("No marks available.")
        return

    highest = max(data, key=lambda x: x[2])
    lowest = min(data, key=lambda x: x[2])
    average = sum(x[2] for x in data) / len(data)

    print("\nPERFORMANCE ANALYSIS")
    print("====================")
    print("Highest:", highest[1], "-", f"{highest[2]:.2f}%")
    print("Lowest:", lowest[1], "-", f"{lowest[2]:.2f}%")
    print("Class Average:", f"{average:.2f}%")

# Main menu loop
def main():
    while True:
        print("""
STUDENT PERFORMANCE ANALYZER
----------------------------
1. Add Student
2. Add Marks
3. Add Attendance
4. Student Report
5. Display Students
6. Performance Analysis
7. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_marks()
        elif choice == "3":
            add_attendance()
        elif choice == "4":
            student_report()
        elif choice == "5":
            display_students()
        elif choice == "6":
            performance_analysis()
        elif choice == "7":
            print("Thank you for using the analyzer!")
            break
        else:
            print("Invalid choice, try again.")
            
main()
