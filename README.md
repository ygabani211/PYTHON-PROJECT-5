# 👨‍💼 Python OOP Employee Management System

A simple **Python OOP (Object-Oriented Programming)** console project for creating and displaying details of a **Person, Employee, and Manager**.

## ✨ Features

- 👤 Create a Person
- 👨‍💻 Create an Employee
- 👨‍💼 Create a Manager
- 📋 Show Person details
- 📋 Show Employee details
- 📋 Show Manager details
- 🚪 Exit the program
- 🔁 Menu-driven console interface

## 🧠 OOP Concepts Used

This project demonstrates:

- 🧱 **Class & Object**
- 🧬 **Inheritance**
- 🔄 **Method Overriding**
- 🔗 **`super()`**
- 🏷️ **Instance Variables**
- 🎯 **Encapsulation through object attributes**

### Class Structure

```text
Person
  │
  └── Employee
        │
        └── Manager
```

- `Person` stores `name` and `age`.
- `Employee` inherits from `Person` and adds `employee_id` and `salary`.
- `Manager` inherits from `Employee` and adds `department`.
- Each class has its own `show_details()` method.

## 📁 Project Structure

```text
Employee_Management_System/
│
├── employee_management_system.py
├── README.md
│
└── screenshots/
    ├── 01_create_person.png
    ├── 02_create_employee.png
    ├── 03_create_manager.png
    └── 04_show_details.png
```

## ▶️ How to Run in VS Code

### 1. Open the project

Open the `Employee_Management_System` folder in **VS Code**.

### 2. Open the Python file

Open:

```text
employee_management_system.py
```

### 3. Run the program

Open the VS Code terminal and run:

```bash
python employee_management_system.py
```

If your system uses `python3`, run:

```bash
python3 employee_management_system.py
```

## 🖥️ Menu

```text
Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
```

## 📸 Screenshots

### 👤 Create a Person

![Create Person](screenshots/01_create_person.png)

### 👨‍💻 Create an Employee

![Create Employee](screenshots/02_create_employee.png)

### 👨‍💼 Create a Manager

![Create Manager](screenshots/03_create_manager.png)

### 📋 Show Details

![Show Details](screenshots/04_show_details.png)

## 🔗 Screenshot URLs for GitHub

After pushing this project to GitHub, these relative image links work directly inside the README:

```text
screenshots/01_create_person.png
screenshots/02_create_employee.png
screenshots/03_create_manager.png
screenshots/04_show_details.png
```

For a GitHub repository named `Employee_Management_System`, the raw-image URL pattern is:

```text
https://raw.githubusercontent.com/YOUR_USERNAME/Employee_Management_System/main/screenshots/01_create_person.png
```

Replace `YOUR_USERNAME` with your GitHub username.

## 📚 What I Learned

This project helps practice:

- Python classes
- Constructors (`__init__`)
- Inheritance
- Method overriding
- User input
- Conditional statements
- `while` loops
- Object creation
- Basic console-based application design

## 👨‍💻 Author

**Your Name**

⭐ If you like this project, you can give the repository a star!
