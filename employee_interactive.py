class Person:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
    
    def get_details(self):
        print(self.name, self.surname, self.email, sep="\n")

class Employee(Person):
    def __init__(self, name, surname, email, employee_id, department):
        super().__init__(name, surname, email)
        self.employee_id = employee_id
        self.department = department
    
    def get_details(self):
        print(self.name, self.surname, self.email, self.employee_id, self.department, sep="\n")
    
my_entries = []

while True:
    choice = input("\nEnter '1' to add a Person, '2' to add an Employee, or 'q' to quit: ")
    try:
        if choice == "q":
            break
        
        name = input("Enter your Name: ").strip().title()
        surname = input("Enter your Surname: ").strip().title()
        email = input("Enter your Email: ").strip()
        
        if choice == "1":
            my_entries.append(Person(name, surname, email))
        elif choice == "2":
            employee_id = input("Enter your Employee ID: ").strip()
            department = input("Enter your Department: ").strip().capitalize()
            my_entries.append(Employee(name, surname, email, employee_id, department))
            break
    except ValueError:
        print("incomplet infomation")
        
print("\n ---Final Report ---")
for entry in my_entries:
    entry.get_details()