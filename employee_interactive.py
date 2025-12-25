class Person:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
    
    def get_details(self):
        print(self.name, self.surname, self.email)

class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department
    
    def get_details(self):
        print(self.name, self.surname, self.email, self.employee_id, self.department)
    
my_entries = []

while True:
    choice = input("\nEnter '1' to add a Person, '2' to add an Employee, or 'q' to quit: ")
    try:
        if choice == "q":
            break
        
        name = input("Enter your Name: ")
        surname = input("Enter your Surname: ")
        email = input("Enter your Email: ")
        
        if choice == "1":
            my_entries.append(Person(name, surname, email))
        elif choice == "2":
            employee_id = input("Enter your Employee ID: ")
            department = input("Enter your Department: ") 
            my_entries.append(Employee(name, surname, email, employee_id, department))
    except ValueError:
        print("incomplet infomation")
        
print("\n ---Final Report ---")
for entry in my_entries:
    print(entry.get_details())