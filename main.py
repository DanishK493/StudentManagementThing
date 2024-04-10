import sys
from managementSystem import ManagementSystem

def main():
    ms = ManagementSystem()
    ms.welcomeMessage()
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
                sys.exit()
main()