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
        pass
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