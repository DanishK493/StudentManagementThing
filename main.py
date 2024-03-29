import sys

class ManagementSystem:
    def __init__(self,students):
        self.students = students
    def welcomeMessage(self):
        path = 'welcome.txt'
        try:
            with open(path,'r',encoding='UTF-8') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"File '{path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    def addStudent(self):
        message = """
==============================Add Student==============================
1. The first letter of firstname and lastname must be capitalized
2. Firstname and lastname must each have at least two letters
3. No digit allowed in the name
4. Student ID is 6 digits long which must start with 700
5. Phone must be in the (xxx-xxx-xxxx) format
6. Student major must be in CS, CYBR, SE, IT, or DS
        """
        print(message)
        id = input("Please enter the student ID: ")
        if len(id) != 6 or not id.startswith('700') or not id.isdigit():
            print("Invalid ID")
            return
        name = input("Please enter the student name (Firstname Lastname): ")
        if not (name.istitle() and len(name.split()) == 2 and name.replace(' ','').isalpha()):
            print("Invalid Name")
            return
        phone = input("Please Enter the Student Phone \u260E: ")
        if not(len(phone) == 12 and phone[3] == '-' and phone[7] == '-' and phone.replace('-','').isdigit()):
            return
        major = input("Please Enter the Student Major: ").upper()
        if major not in ['CS','CYBR','SE','IT','DS']:
            print("Invalid Major")
            return
        self.students.append({
            "ID": id,
            "Name": name,
            "Phone": phone,
            "Major": major
        })
        print("\u2714 New student record has been added")
    def delStudent(self):
        pass
    def modifyStudent(self):
        pass
    def showStudent(self):
        pass
    def displayStudents(self):
        pass
def main():
    students = [
        {"ID":"700001","Name":"Danish Khateeb","Phone":"000-000-0000","Major":"CS"}
         ]
    ms = ManagementSystem(students)
    ms.welcomeMessage()
    while True:
        choice = int(input("Please Enter the Operation Code: "))
        match choice:
            case 1:
                ms.addStudent()
            case 2:
                ms.showStudent()
            case 3:
                ms.modifyStudent()
            case 4:
                ms.delStudent()
            case 5:
                ms.displayStudents()
            case 6:
                sys.exit()
main()