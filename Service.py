from Data import courses
from Data import addCourse, cursor, commit
from print_level import print_success, print_red

def showAllCourse():
    for index, course in enumerate(courses, start = 1):
        print(f"{index}: {course}")

@commit
def addCourseQuery():
    title = input("Title: ")
    description = input("Description: ")
    mentor = input("Mentor: ")
    duration = input("Duration: ")
    price = input("Price: ")
    finished = input("Is Finished: ")

    queryParam = (title, description, mentor, duration, price, finished)

    cursor.execute(addCourse, queryParam)

    print_success("Course Saved!")

@commit
def updateCourseQuery():
    showAllCourse()

    id = int(input("ID => "))

    course = cursor.execute(f"""select * from courses where id = {id}""").fetchone()

    if not course:
        print_red("Wrong Choice!")
    else:
        title = input("Title: ")
        description = input("Description: ")
        mentor = input("Mentor: ")
        duration = input("Duration: ")
        price = input("Price: ")
        finished = input("Is Finished: ")

        cursor.execute(f"""
            update courses set title = '{title}', description = '{description}', mentor = '{mentor}', duration = '{duration}', price = '{price}', finished = '{finished}' where id = {id}
        """)

        print_success("Successfully Updated!")

@commit
def deleteCourse():
    showAllCourse()

    id = int(input("ID => "))

    course = cursor.execute(f"""select * from courses where id = {id}""").fetchone()

    if not course:
        print_red("Wrong Choice!")
    else:
        cursor.execute(f"""
            delete from courses where id = {id}
        """)

        print_success("Successfully Deleted!")