# Project Statement

## 1. Problem Statement

Managing student academic performance manually can be time-consuming and may lead to calculation errors. Teachers and students need a simple way to record student details, marks, attendance, and analyze overall performance.

The **Student Performance Analyzer** is developed to provide a simple, menu-driven Python application that stores student information and automatically calculates marks, grades, attendance percentages, and performance levels. It also provides class-level performance analysis to make academic evaluation easier and more organized.

## 2. Scope of the Project

The project focuses on basic student performance management using Python. It allows users to:

* Register student details.
* Store student information using roll numbers.
* Add marks for multiple subjects.
* Calculate average marks and grades.
* Record and calculate attendance.
* Generate individual student performance reports.
* Display a list of registered students.
* Analyze class performance.
* Identify the highest and lowest performing students.
* Calculate the overall class average.

The current version is a **console-based application** and stores data temporarily while the program is running. Future versions can include permanent data storage, databases, graphical interfaces, and report exporting.

## 3. Target Users

The main target users of this project are:

* **Teachers** – to record and analyze student academic performance.
* **Students** – to check their marks, grades, attendance, and performance.
* **Educational Institutions** – for basic academic performance tracking.
* **Beginners learning Python** – to understand how programming concepts can be applied to a real-world problem.

## 4. High-Level Features

### Student Management

* Add new student records.
* Store name, roll number, branch, and semester.
* Prevent duplicate roll numbers.
* Display all registered students.

### Marks Management

* Add marks for multiple subjects.
* Validate marks between 0 and 100.
* Calculate total and average marks.
* Automatically assign grades.

### Attendance Management

* Record total classes and attended classes.
* Calculate attendance percentage.
* Display attendance status.

### Student Report

* Generate a detailed report for an individual student.
* Display subject-wise marks.
* Show average, grade, attendance, and performance.
* Identify the best and weakest subject.

### Performance Analysis

* Find the highest-performing student.
* Find the lowest-performing student.
* Calculate the class average.
* Provide an overview of class performance.

### Input Validation

* Detect invalid marks.
* Prevent invalid attendance values.
* Handle incorrect numerical inputs.
* Check whether a student exists before adding marks or attendance.
