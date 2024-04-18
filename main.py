import sys
from managementSystem import ManagementSystem

#main system
def main():
    #create an instance of the ManagementSystem class
    ms = ManagementSystem()
    #print welcome message
    ms.welcomeMessage()
    #start of main loop
    while True:
        choice = int(input("Please Enter the Operation Code: "))
        match choice:
            case 1:
                ms.addStudent()
            case 2:
                ms.delStudent()
            case 3:
                ms.modifyStudent()
            case 4:
                ms.showStudent()
            case 5:
                ms.displayStudents()
            case 6:
                ms.displayStudentsInMajor()
            case 7:
                ms.absences()
            case 8:
                sys.exit()
main()