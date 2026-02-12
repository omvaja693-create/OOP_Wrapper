# -------------------------------
# Employee Management System
# -------------------------------

class Employee:
    company_name = "ABC Corp"   # Class variable

    def __init__(self, employee_id=None, name=None, age=None, salary=0.0):
        # Encapsulation (private attributes)
        self.__employee_id = employee_id
        self.__name = name
        self.__age = age
        self.__salary = salary

    # Destructor
    def __del__(self):
        print(f"Employee object {self.__name} is being deleted.")

    # Getters
    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    # Setters
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative!")

    # Method Overriding Target
    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Employee ID:", self.__employee_id)
        print("Salary: $", self.__salary)


# -------------------------------
# Manager Class
# -------------------------------

class Manager(Employee):
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):   # Method Overriding
        super().display()
        print("Department:", self.department)


# -------------------------------
# Developer Class
# -------------------------------

class Developer(Employee):
    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):   # Method Overriding
        super().display()
        print("Programming Language:", self.programming_language)


# -------------------------------
# Main Menu (User Interface)
# -------------------------------

def main():
    person = None
    employee = None
    manager = None
    developer = None

    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("1. Create an Employee")
        print("2. Create a Manager")
        print("3. Create a Developer")
        print("4. Show Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))

            employee = Employee(emp_id, name, age, salary)
            print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}")

        elif choice == "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")

            manager = Manager(emp_id, name, age, salary, dept)
            print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, department: {dept}")

        elif choice == "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")

            developer = Developer(emp_id, name, age, salary, lang)
            print(f"\nDeveloper created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, language: {lang}")

        elif choice == "4":
            print("\nChoose details to show:")
            print("1. Employee")
            print("2. Manager")
            print("3. Developer")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1" and employee:
                employee.display()
            elif sub_choice == "2" and manager:
                manager.display()
            elif sub_choice == "3" and developer:
                developer.display()
            else:
                print("No data available!")

        elif choice == "5":
            print("Exiting the system. All resources have been freed.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


# issubclass() check demonstration
print("Is Manager subclass of Employee?", issubclass(Manager, Employee))
print("Is Developer subclass of Employee?", issubclass(Developer, Employee))


# Run Program
main()
