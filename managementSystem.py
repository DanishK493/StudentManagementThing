import json

class ManagementSystem:
    def __init__(self):
        with open('student.json','r') as f:
            self.students = json.load(f)
    def welcomeMessage(self):
        path = 'welcome.txt'
        try:
            with open(path,'r',encoding='UTF-8') as file:
                content = file.read()
                print(content) # print welcome menu
        except Exception as e:
            print(f"An error occurred: {e}")
    def addStudent(self):
        path = 'addstudent.txt'
        try:
            with open(path,'r') as file:
                content = file.read()
                print(content) #print add student menu
        except Exception as e:
            print(f"An error occurred: {e}")
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
            "Major": major,
            "Absences": 0
        })
        print("\u2714 New student record has been added!")
        #updates json file
        with open('student.json', 'w') as f:
            json.dump(self.students, f, indent=4)
    #deletes student record
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
                        print("Student record has been deleted")
            #if user is not sure, it passes
            else:
                pass
        #updates json file
        with open('student.json', 'w') as f:
            json.dump(self.students, f, indent=4)
    def modifyStudent(self):
        #enter student id to modify
        id = input("Please Enter Student ID to Modify: ")
        #checks for student id in students
        student = next((s for s in self.students if s["ID"] == id),None)
        counter = 0
        #if student id exists
        if student:
            #gives new name, phone, and major
            name = input("New name: ")
            phone = input("New phone: ")
            major = input("New major: ")
            #checks if name is valid
            if  (name.istitle() and len(name.split()) == 2 and name.replace(' ','').isalpha()):
                student["Name"] = name
                #adds a count if name is modified
                counter+=1
            #checks if phone is valid
            if (len(phone) == 12 and phone[3] == '-' and phone[7] == '-' and phone.replace('-','').isdigit()):
                student["Phone"] = phone
                #adds a count if phone is modified
                counter+=1
            #checks if major is valid
            if major.upper() in ['CS','CYBR','SE','IT','DS']:
                student["Major"] = major.upper()
                #adds a count if major is modified
                counter+=1
            #if any of the fields are modified
            if counter != 0:
                print("\u2714 Student record has been modified!")
            else:
                print("\u274C No modifications were made")
        #if student id doesn't exist
        else:
            print(f"Student ID {id} doesn't exist")
        #updates json file
        with open('student.json', 'w') as f:
            json.dump(self.students, f, indent=4)
        
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
                    print(f"{'ID':<20s}{'Name':<20s}{'Phone':<20s}{'Major':<20s}{'Absences':<20s}")
                    print(f"{i['ID']:<20}{i['Name']:<20s}{i['Phone']:<20s}{i['Major']:<20s}{str(i['Absences']):<20s}")
    def displayStudents(self):
        #prints all students
        print("Student Record")
        print(f"{'ID':<20s}{'Name':<20s}{'Phone':<20s}{'Major':<20s}{'Abesences':<20s}")
        for student in self.students:
            print(f"{student['ID']:<20}{student['Name']:<20s}{student['Phone']:<20s}{student['Major']:<20s}{str(student['Absences']):<20s}")
    def absences(self):
        #enter ID of student to count absent
        ID = input("Enter the ID of the student you want to count absent: ")
        #checks if ID is in students
        student = next((s for s in self.students if s["ID"] == ID),None)
        #if student doesn't exist
        if student is None:
            print(f"Student ID {ID} doesn't exist")
        #if student exists
        else:
            #absent is counted
            student["Absences"] += 1
            print("Absence added")
        #json file is updated
        with open('student.json', 'w') as f:
            json.dump(self.students, f, indent=4)
        
    def displayStudentsInMajor(self):
        #prints all students taking a specific course
        major = input("Enter major: ").upper()
        print(f"Students in {major}:")
        for student in self.students:
            if student['Major'] == major:
                print(f"{student['Name']:<20s}")

        