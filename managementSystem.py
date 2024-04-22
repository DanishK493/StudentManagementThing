import re
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from data import User, Student, Score

class ManagementSystem:
    def __init__(self):
        self.engine = create_engine('sqlite:///students.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    def loginMessage(self):
        self.read_and_print_file('login.txt')
            
        
    def register(self):
        print("==============================Register==============================\n1. Account name is between 3 and 6 letters long\n2. Account name's first letter must be capitalized")
        while True:
            username = input("Please Enter Account Name: ")
            existing_user = self.session.query(User).filter_by(name=username).first()
            if existing_user:
                print("Registration Failed! Account Already Exists")
            elif not ((len(username) >= 3 and len(username) <= 6) and username.isalnum()):
                print("Account Name Not Valid!")
            else:
                break
    
        print("1. Password must start with one of the following special characters !@#$%^&*")
        print("2. Password must contain at least one digit, one lowercase letter, and one uppercase letter")
        print("3. Password is between 6 and 12 letters long")

        while True:
            password = input("Please enter your password: ")
            if not re.match(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,12}$", password):
                print("Password Not Valid!")
            else:
                break

        new_user = User(name=username, password=password)
        self.session.add(new_user)

        # Commit the changes
        self.session.commit()
        print("Registration completed!")
        self.welcomeMessage()
        
    def login(self):
        print("==============================Login==============================")
        username = input("Please Enter Your Account Username: ")
        user = self.session.query(User).filter_by(name=username).first()
        while not user:
            print("Login Failed! Account Doesn't Exist")
            username = input("Please Enter Your Account Username: ")
            user = self.session.query(User).filter_by(name=username).first()
        password = input("Please Enter Your Account Password: ")    
        while password != user.password:
            print("Invalid password")
            password = input("Please Enter Your Account Password: ")
        self.welcomeMessage()
    def read_and_print_file(self, path):
        try:
            with open(path,'r',encoding='UTF-8') as file:
                content = file.read()
                print(content)
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def welcomeMessage(self):
        self.read_and_print_file('welcome.txt')
        
    def addStudent(self):
        self.read_and_print_file('addstudent.txt')
        name = input("Please enter the student name (Firstname Lastname): ")
        if not (name.istitle() and len(name.split()) == 2 and all(len(part) >= 2 for part in name.split()) and name.replace(' ','').isalpha()):
            print("Invalid Name")
            return
        age = input("Please Enter Student's Age: ")
        if not (int(age) > 0 and int(age) < 100):
            print("Invalid age")
            return
        gender = input("Please Enter Student's Gender: ").upper()
        if not(gender == 'M' or gender == 'F' or gender == 'O'):
            print("Invalid Gender")
            return
        phone = input("Please Enter the Student Phone \u260E: ")
        if not(len(phone) == 12 and phone[3] == '-' and phone[7] == '-' and phone.replace('-','').isdigit()):
            print("Invalid Phonenumber")
            return
        major = input("Please Enter the Student Major: ").upper()
        if major not in ['CS','CYBR','SE','IT','DS']:
            print("Invalid Major")
            return
        id = str(700300000 + self.session.query(Student).count() + 1)

        print("\u2714 New student record has been added!")
        new_student = Student(id=id, name=name, age=age, gender=gender, major=major, phone=phone)
        self.session.add(new_student)

        new_score = Score(id=id, name=name, CS1030=0, CS1100=0, CS2030=0)
        self.session.add(new_score)

        self.session.commit()
    #deletes student record
    def delStudent(self):
        #enter ID of student to delete
        ID = input("Enter the ID of the student you want to delete: ")
        student = self.session.query(Student).filter(Student.id == ID).first()
        score = self.session.query(Score).filter(Score.id == ID).first()

        #if ID is not in students
        if student is None:
            print(f"Student ID {ID} doesn't exist") 
        #if ID is in students
        else:
            print(f"{'ID':<20s}{'Name':<20s}{'Phone':<20s}{'Major':<20s}{'Absences':<20s}")
            print(f"{student.id:<20s}{student.name:<20s}{student.age:<20d}{student.gender:<20s}{student.major:<20s}{student.phone:<20s}")
            #checks if user is sure
            q = input("Are you sure you want to delete the record? Y or N: ")
            #if user is sure, it deletes the record
            if q.upper() == "Y":
                self.session.delete(student)
                if score is not None:
                    self.session.delete(score)
                self.session.commit()
                print("Student record has been deleted")
            #if user is not sure, it passes
            else:
                pass
        #updates json file

    def modifyStudent(self):
        #enter student id to modify
        id = input("Please Enter Student ID to Modify: ")
        #checks for student id in students
        student = self.session.query(Student).filter_by(id=id).first()
        counter = 0
        #if student id exists
        if student:
            #gives new name, phone, and major
            name = input("New name: ")
            phone = input("New phone: ")
            major = input("New major: ")
            #checks if name is valid
            if  (name.istitle() and len(name.split()) == 2 and name.replace(' ','').isalpha()):
                student.name = name
                #adds a count if name is modified
                counter+=1
            #checks if phone is valid
            if (len(phone) == 12 and phone[3] == '-' and phone[7] == '-' and phone.replace('-','').isdigit()):
                student.phone = phone
                #adds a count if phone is modified
                counter+=1
            #checks if major is valid
            if major.upper() in ['CS','CYBR','SE','IT','DS']:
                student.major = major.upper()
                #adds a count if major is modified
                counter+=1
            #if any of the fields are modified
            if counter != 0:
                print("\u2714 Student record has been modified!")
                self.session.commit()
            else:
                print("\u274C No modifications were made")
        #if student id doesn't exist
        else:
            print(f"Student ID {id} doesn't exist")
        
    def showStudentbyID(self):
        #enter ID of student to show
        id = input("Please enter the Student ID you want to query: ")
        student = self.session.query(Student).filter_by(id=id).first()
        if student:
            print("==============================Student Record==============================")
            print(f"{'ID':<20s}{'Name':<20s}{'Age':<20s}{'Gender':<20s}{'Major':<20s}{'Phone':<20s}")
            print(f"{student.id:<20s}{student.name:<20s}{student.age:<20d}{student.gender:<20s}{student.major:<20s}{student.phone:<20s}")
        else:
            print(f"\u274C Student with ID {id} not found")
    def displayStudents(self):
        #prints all students
        print("Student Record")
        print(f"{'ID':<20s}{'Name':<20s}{'Age':<20s}{'Gender':<20s}{'Major':<20s}{'Phone':<20s}")
        students = self.session.query(Student).all()
        for student in students:
            print(f"{student.id:<20s}{student.name:<20s}{student.age:<20d}{student.gender:<20s}{student.major:<20s}{student.phone:<20s}")
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

        
    def displayStudentsInMajor(self):
        #prints all students taking a specific course
        major = input("Enter major: ").upper()
        print(f"Students in {major}:")
        for student in self.students:
            if student['Major'] == major:
                print(f"{student['Name']:<20s}")
    
    def showStudentGrade(self):
        #enter name of student
        name = input("Enter the name of the student you want to show: ")
        student = next((s for s in self.students if s["Name"] == name),None)
        if student is None:
            print(f"Student {name} doesn't exist")
        #if student exists
        else:
            print(f"{'ID':<20s}{'Name':<20s}{'CS 1100':<20s}{'CS 1200':<20s}{'CS 1300':<20s}")
            #for i in self.students:
                #if i["Name"] == name:
                    #print(f"{i['ID']:<20}{i['Name']:<20s}{'A':<20s}{'B':<20s}{'C':<20s}")
    def login_register(self):
        while True:
            self.loginMessage()
            choice = input("Please select (1 - 3): ")
            if choice == '1':
                self.login()
                return
            elif choice == '2':
                self.register()
                return
            elif choice == '3':
                sys.exit()
            else:
                print("Invalid Choice.")
    def operations(self):
        while True:
            #print welcome message
            self.welcomeMessage()
            choice = int(input("Please Enter the Operation Code: "))
            match choice:
                case 1:
                    self.addStudent()
                case 2:
                    self.delStudent()
                case 3:
                    self.modifyStudent()
                case 4:
                    self.showStudentMenu()
                    choice2 = int(input("Please Enter the Operation Code: "))
                    match choice2:
                        case 1:
                            self.showStudentbyID()
                        case 2:
                            self.showStudentbyName()
                        case 3:
                            self.displayStudents()
                        case 4:
                            self.displayStudentsInMajor()
                case 5:
                    self.absences()
                case 6:
                    sys.exit()