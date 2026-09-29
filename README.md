# Student Performance Analyzer

## 1. Project Overview

The **Student Performance Analyzer** is a Python-based console application designed to manage and analyze student academic performance.

The project allows users to store student details, enter subject-wise marks, record attendance, generate individual student reports, and analyze the overall performance of a class.

The application uses a simple menu-driven interface, making it easy to operate and suitable for beginners learning Python programming.

## 2. Features

* Add new student details.
* Prevent duplicate roll numbers.
* Add marks for multiple subjects.
* Validate marks between 0 and 100.
* Calculate total and average marks.
* Automatically calculate student grades.
* Record total and attended classes.
* Calculate attendance percentage.
* Display attendance status.
* Generate detailed student reports.
* Identify the best and weakest subjects.
* Display all registered students.
* Analyze class performance.
* Find the highest and lowest performing students.
* Calculate the class average.
* Handle invalid user inputs.

## 3. Technologies / Tools Used

### Programming Language

* **Python 3**

### Python Concepts Used

* Functions
* Dictionaries
* Loops
* Conditional statements
* Exception handling
* User input
* Data validation
* Lambda functions

### Development Tools

* **Visual Studio Code / PyCharm / IDLE**
* **Git**
* **GitHub**

No external Python libraries are required to run the project.

## 4. Installation and Running

### Step 1: Install Python

Download and install **Python 3** on your computer.

Check whether Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Clone the Repository

Clone the GitHub repository using:

```bash
git clone https://github.com/amangupta14-gif/Student-Performance-Analyzer.git
```

### Step 3: Open the Project Folder

```bash
cd Student-Performance-Analyzer
```

### Step 4: Run the Program

Run the Python file:

```bash
python student_performance.py
```

If your system uses `python3`, run:

```bash
python3 student_performance.py
```

The application will display the main menu in the terminal.

## 5. How to Use the Project

After starting the program, the following menu will appear:

```text
STUDENT PERFORMANCE ANALYZER
----------------------------
1. Add Student
2. Add Marks
3. Add Attendance
4. Student Report
5. Display Students
6. Performance Analysis
7. Exit
```

Select an option by entering its corresponding number.

For example:

1. Select **Add Student** to register a student.
2. Select **Add Marks** to enter subject-wise marks.
3. Select **Add Attendance** to enter attendance details.
4. Select **Student Report** to view a student's complete performance.
5. Select **Performance Analysis** to view class-level statistics.
6. Select **Exit** to close the application.

## 6. Testing Instructions

The project can be tested manually through the console.

### Test 1: Add Student

Select:

```text
1. Add Student
```

Enter valid student information such as:

```text
Roll Number: 101
Name: Rahul
Branch: CSE
Semester: 2
```

**Expected Result:**

```text
Student added!
```

### Test 2: Duplicate Student

Try adding another student using the same roll number.

**Expected Result:**

```text
Student already exists!
```

### Test 3: Add Marks

Select:

```text
2. Add Marks
```

Enter a valid roll number and subject marks between 0 and 100.

**Expected Result:**

```text
Marks added!
```

### Test 4: Invalid Marks

Enter a mark outside the range of 0–100.

For example:

```text
Marks (0-100): 120
```

**Expected Result:**

```text
Marks must be between 0 and 100.
```

### Test 5: Add Attendance

Select:

```text
3. Add Attendance
```

Enter valid total and attended classes.

For example:

```text
Total classes: 40
Classes attended: 35
```

**Expected Result:**

```text
Attendance: 87.50%
```

### Test 6: Invalid Attendance

Enter attended classes greater than total classes.

For example:

```text
Total classes: 40
Classes attended: 45
```

**Expected Result:**

```text
Invalid attendance!
```

### Test 7: Generate Student Report

Select:

```text
4. Student Report
```

Enter an existing roll number.

**Expected Result:**

The program displays:

* Student name
* Roll number
* Branch
* Semester
* Subject-wise marks
* Total marks
* Average percentage
* Grade
* Attendance percentage
* Attendance status
* Best subject
* Weakest subject
* Overall performance

### Test 8: Performance Analysis

Add marks for multiple students and select:

```text
6. Performance Analysis
```

**Expected Result:**

The program displays:

* Highest-performing student
* Lowest-performing student
* Class average

### Test 9: Invalid Menu Choice

Enter an option that is not between 1 and 7.

For example:

```text
Enter choice: 9
```

**Expected Result:**

```text
Invalid choice, try again.
```

## 7. Expected Outcome

After successful execution and testing, the application should correctly store student information during the program session, calculate academic performance and attendance, generate student reports, and provide class-level performance analysis.

## 8. Project Limitations

* Data is stored only while the program is running.
* The application currently uses a console-based interface.
* No database is connected.
* Data is not automatically saved after the program is closed.

## 9. Future Enhancements

Future versions could include:

* Database integration.
* Permanent data storage.
* Graphical user interface.
* Student record editing and deletion.
* Exporting reports to PDF or Excel.
* User login and authentication.
* Graphical performance charts.

## 10. Author

AMAN KUMAR GUPTA

---

⭐ If you find this project useful, consider giving the repository a star.
