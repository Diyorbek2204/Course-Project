import sqlite3

connection = sqlite3.connect("Course.db")
cursor = connection.cursor()

cursor.execute("""
        create table if not exists Courses(
            id integer primary key,
            title varchar,
            description varchar,
            mentor varchar,
            duration varchar,
            price float,
            finished varchar
        );
""")

addCourse = """
    insert into Courses(title, description, mentor, duration, price, finished) values(?, ?, ?, ?, ?, ?)
"""

courses = cursor.execute("""
    select * from Courses
""").fetchall()

def commit(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        connection.commit()
        return response
    return wrapper