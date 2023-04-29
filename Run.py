from colorama import Fore
from Menu import menu
from Service import addCourseQuery, updateCourseQuery, showAllCourse, deleteCourse

def run():
    while True:
        choice = menu()

        if choice == "1":
            showAllCourse()
        elif choice == "2":
            addCourseQuery()
        elif choice == "3":
            updateCourseQuery()
        elif choice == "4":
            deleteCourse()
        elif choice == "5":
            quit(Fore.RED + "Program Closed!")
        else:
            print("Wrong Choice!!! Enter [1, 2, 3, 4, 5]")

run()