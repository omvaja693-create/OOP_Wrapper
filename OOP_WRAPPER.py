
#============================================================class========================================================================================================================
class Employee:
    def __init__(self, name, age, emp_id, salary):
        self.__employee_id = emp_id
        self.__name = name
        self.__age = age
        self.__salary = salary

    def Emp(self):
        print(f"Employee`s id:{self.__employee_id} | Employee`s Name: {self.__name} | Employee`s Age: {self.__age} | Employee`s Salary: {self.__salary}")


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, dept):
        super().__init__(name, age, emp_id, salary)   
        self.__Department = dept

    def Man(self):
        super().Emp()   
        print(f"Employee`s Dept: {self.__Department}")


class Developer(Employee):
    def __init__(self, name, age, emp_id, salary, lang):
        super().__init__(name, age, emp_id, salary)   
        self.__language = lang

    def Dev(self):
        super().Emp()   
        print(f"Employee`s Language: {self.__language}")


#==========================================================program=======================================================================================================================

print('--- Python OOP Project: Employee Management System ---')

employee = None
manager = None
developer = None

while True:
    print()
    print('Choose an operation:')
    print('1. Create a Person')
    print('2. Create a Manager')
    print('3. Create a Developer')
    print('4. Show Details')
    print('5. Exit')
    print()

    choise = int(input('Enter your choise: '))
    print()

    match choise:

        case 1:
            name = input('Enter Employee`s name: ')
            age = int(input('Enter Employee`s Age: '))
            emp_id = input("Enter Employee ID: ")
            salary = int(input('Enter Employee`s Salary: '))

            employee = Employee(name, age, emp_id, salary)
            print(f"Person Name {name} Created Successfully...")

        case 2:
            name = input('Enter Employee`s name: ')
            age = int(input('Enter Employee`s Age: '))
            emp_id = input("Enter Employee ID: ")
            salary = int(input('Enter Employee`s Salary: '))
            dept = input("Enter Department: ")

            manager = Manager(name, age, emp_id, salary, dept)
            print(f"Manager Name {name} Created Successfully...")

        case 3:
            name = input('Enter Employee`s name: ')
            age = int(input('Enter Employee`s Age: '))
            emp_id = input("Enter Employee ID: ")
            salary = int(input('Enter Employee`s Salary: '))
            lang = input("Enter Programming Language: ")

            developer = Developer(name, age, emp_id, salary, lang)
            print(f"Developer Name {name} Created Successfully...")

        case 4:
            print("Choose Detail To Show...")
            print("1. Person")
            print("2. Manager")
            print("3. Developer")

            choise = int(input("Enter your choise: "))

            match choise:
                case 1:
                    if employee:
                        employee.Emp()
                    else:
                        print("No Person Created Yet.")

                case 2:
                    if manager:
                        manager.Man()
                    else:
                        print("No Manager Created Yet.")

                case 3:
                    if developer:
                        developer.Dev()
                    else:
                        print("No Developer Created Yet.")

        case 5:
            print("Exiting the system. Goodbye!")
            break

        case _:
            print("Invalid Choice...")










            

