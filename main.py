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
        #enter ID of student to delete
        ID = input("Enter the ID of the student you want to delete: ")
        #counter for if ID is in students
        length = 0
        for i in self.students:
            if i["ID"] != ID:
                 length += 1
            else:
                #breaks if ID is found
                break
        #if ID is not in students
        if length == len(self.students):
            print("The student ID does not exist")
        #if ID is in students
        else:
            #*add print student record
            #checks if user is sure
            q = input("Are you sure you want to delete the record? Y or N: ")
            #if user is sure, it deletes the record
            if q.upper() == "Y":
                for i in range(len(self.students)-1):
                    if self.students[i]["ID"] == ID:
                        del self.students[i]
            #if user is not sure, it passes
            else:
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