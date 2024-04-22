import sys
from managementSystem import ManagementSystem

#main system
def main():
    #create an instance of the ManagementSystem class
    ms = ManagementSystem()
    #start of main loop
    while True:
        #print welcome message
        ms.welcomeMessage()
        choice = int(input("Please Enter the Operation Code: "))
        match choice:
            case 1:
                ms.addStudent()
            case 2:
                ms.delStudent()
            case 3:
                ms.modifyStudent()
            case 4:
                ms.showStudentMenu()
                choice2 = int(input("Please Enter the Operation Code: "))
                match choice2:
                    case 1:
                        ms.showStudentbyID()
                    case 2:
                        ms.showStudentbyName()
                    case 3:
                        ms.displayStudents()
                    case 4:
                        ms.displayStudentsInMajor()
            case 5:
                ms.absences()
            case 6:
                sys.exit()
main()