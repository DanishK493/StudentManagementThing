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
        if len(id) != 6 or not id.startswith('700') or not id.isdigit(): # prints invalid if id isnt a 6 in length, doesnt start with 700, or isnt a digit
            print("\u274C Invalid ID")
            return
        name = input("Please enter the student name (Firstname Lastname): ")
        if not (name.istitle() and len(name.split()) == 2 and name.replace(' ','').isalpha()): # prints invalid if name doesnt start with uppercase or name includes numbers
            print("\u274C Invalid Name")
            return
        phone = input("Please Enter the Student Phone \u260E: ")
        if not(len(phone) == 12 and phone[3] == '-' and phone[7] == '-' and phone.replace('-','').isdigit()): #prints invalid if len isnt 12 or dashes are missing or letters are included
            print("\u274C Invalid Number")
            return
        major = input("Please Enter the Student Major: ").upper()
        if major not in ['CS','CYBR','SE','IT','DS']: #prints invalid if major is not one of these
            print("\u274C Invalid Major")
            return
        self.students.append({
            "ID": id,
            "Name": name,
            "Phone": phone,
            "Major": major
        })
        print("\u2714 New student record has been added!")
    def delStudent(self):
        #enter ID of student to delete
        ID = input("Enter the ID of the student you want to delete: ")
        student = next((s for s in self.students if s["ID"] == ID),None)
        #if ID is not in students
        if student is None:
            print(f"Student ID {ID} doesn't exist") 
        #if ID is in students
        else:
            #*add print student record
            #checks if user is sure
            q = input("Are you sure you want to delete the record? Y or N: ")
            #if user is sure, it deletes the record
            if q.upper() == "Y":
                for i in range(len(self.students)-1 if len(self.students) > 1 else 1):
                    if self.students[i]["ID"] == ID:
                        del self.students[i]
            #if user is not sure, it passes
            else:
                pass
    def modifyStudent(self):
        id = input("Please Enter Student ID to Modify: ")
        student = next((s for s in self.students if s["ID"] == id),None)
        if student:
            pass
        else:
            print(f"Student ID {id} doesn't exist")
    def showStudent(self):
        #enter ID of student to show
        ID = input("Enter the ID of the student you want to show: ")
        student = next((s for s in self.students if s["ID"] == ID),None)
        if student is None:
            print(f"Student ID {ID} doesn't exist")
        #if ID is in students
        else:
            #prints single ID
            for i in self.students:
                if i["ID"] == ID:
                    print(i)
    def displayStudents(self):
        print("Student Record")
        print(f"{'ID':<20s}{'Name':<20s}{'Phone':<20s}{'Major':<20s}")
        for student in self.students:
            print(f"{student['ID']:<20}{student['Name']:<20s}{student['Phone']:<20s}{student['Major']:<20s}")
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