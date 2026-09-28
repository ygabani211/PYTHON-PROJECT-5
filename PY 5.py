
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("\nPerson Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = float(salary)

    def show_details(self):
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def show_details(self):
        print("\nManager Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")


def main():
    person_record = None
    employee_record = None
    manager_record = None

    print("--- Python OOP Project: Employee Management System ---")

    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("\nEnter Name: ")
            age = input("Enter Age: ")
            person_record = Person(name, age)
            print(f"\nPerson created with name: {name} and age: {age}.")
            
        elif choice == '2':
            name = input("\nEnter Name: ")
            age = input("Enter Age: ")
            emp_id = input("Enter Employee ID: ")
            salary = input("Enter Salary: ")
            employee_record = Employee(name, age, emp_id, salary)
            print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${float(salary)}.")
            
        elif choice == '3':
            name = input("\nEnter Name: ")
            age = input("Enter Age: ")
            emp_id = input("Enter Employee ID: ")
            salary = input("Enter Salary: ")
            department = input("Enter Department: ")
            manager_record = Manager(name, age, emp_id, salary, department)
            print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${float(salary)}, and department: {department}.")
            
        elif choice == '4':
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            detail_choice = input("Enter your choice: ")

            if detail_choice == '1':
                if person_record:
                    person_record.show_details()
                else:
                    print("\nNo Person created yet.")
            elif detail_choice == '2':
                if employee_record:
                    employee_record.show_details()
                else:
                    print("\nNo Employee created yet.")
            elif detail_choice == '3':
                if manager_record:
                    manager_record.show_details()
                else:
                    print("\nNo Manager created yet.")
            else:
                print("\nInvalid detail choice.")
                
        elif choice == '5':
            print("\nExiting the system. All resources have been freed.")
            print("\nGoodbye!")
            break
            
        else:
            print("\nInvalid choice. Please select a valid option.")

        print("\n--- Choose another operation ---")


if __name__ == "__main__":
    main()