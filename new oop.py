#============================================================class===============================================================
class Employee:
    def __init__(self,emp_id, name, age, salary):
        self.__employee_id = emp_id
        self.__name = name
        self.__age = age
        self.__salary = salary

    def getdata(self):
        print(f"Employee`s id:{self.__employee_id} | Employee`s Name: {self.__name} | Employee`s Age: {self.__age} | Employee`s: {self.__salary}")

class Manager(Employee):
    def __init__(self, emp_id, name, age, salary, department):
        self.__employee_id = emp_id
        self.__name = name
        self.__age = age
        self.__salary = salary

        self.__Department = department

    def getdata(self):
        print(f"Employee`s id:{self.__employee_id} | Employee`s Name: {self.__name} | Employee`s Age: {self.__age} | Employee`s: {self.__salary} | Employee`s Department: {self.Department}")

class Developer(Employee):
    def __init__(self):
        self.__employee_id = int(input('Enter Employee`s id: '))
        self.__name = input('Enter Employee`s Name: ')
        self.__age = int(input('Enter Employee`s Age: '))
        self.__salary = int(input('Enter Employee`s Salary: '))
        self.__Developer = input('Enter Employee`s Language: ')

      def getdata(self):
        print(f"Employee`s id:{self.__employee_id} | Employee`s Name: {self.__name} | Employee`s Age: {self.__age} | Employee`s: {self.__salary} | Employee`s Language: {}

#==========================================================program===============================================================

print('--- Python OOP Project: Employee Management System ---')

while True:
    print()
    print('Choose an operation:')
    print('1. Create a Person')
    print('2. Create an Employee:)
    print('3. Create a Manager')
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
        
              employee = Employee(emp_id, name, age, salary)
              print(f"Employee Name {name} Created Sucessfully...")
          case 2:
          case 3:pass
          case 4:pass
          case 5:break
          case _:

