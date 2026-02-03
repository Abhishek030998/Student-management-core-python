from students.models import Student
from students import db, utils

DATA_FILE = 'students.csv'


def createStudent():
    # Interactive creation with validation
    students = db.load_students(DATA_FILE)
    existing_ids = set(s.id for s in students)
    sid = utils.generate_id(existing_ids)
    name = input('Name: ').strip()
    while True:
        email = input('Email: ').strip()
        if utils.validate_email(email):
            break
        print('Invalid email format. Try again.')
    def read_mark(prompt):
        while True:
            v = input(prompt).strip()
            if v.isdigit() and 0 <= int(v) <= 100:
                return int(v)
            print('Enter integer marks between 0 and 100')
    eng = read_mark('English marks: ')
    maths = read_mark('Maths marks: ')
    science = read_mark('Science marks: ')
    dob = input('Date of Birth (YYYY-MM-DD): ').strip()

    student = Student(id=sid, name=name, email=email, eng=eng, maths=maths, science=science, dob=dob)
    db.add_student(DATA_FILE, student)
    print(f'Created student {student.id} - {student.name}')


def findStudentByName():
    q = input('Enter name or part of name: ').strip()
    results = db.find_by_name(DATA_FILE, q)
    for s in results:
        print(s)
    if not results:
        print('No student found')


def list_top_students():
    above = db.students_above_percentage(DATA_FILE, 80.0)
    for s in above:
        print(f"{s.id} {s.name} {s.percentage}%")


def removeStudent():
    sid = input('Enter student id to remove: ').strip()
    ok = db.remove_student_by_id(DATA_FILE, sid)
    print('Removed' if ok else 'Not found')


def age_of_student():
    sid = input('Enter student id to get age: ').strip()
    students = db.load_students(DATA_FILE)
    for s in students:
        if s.id == sid:
            print(f"{s.name} is {s.age()} years old")
            return
    print('Student not found')


if __name__ == '__main__':
    import os
    if not os.path.exists(DATA_FILE):
        utils.generate_sample_data(20, DATA_FILE)
        print('Sample data created in students.csv')
    print('\n--- Top students (>80%) ---')
    list_top_students()
    print('\nAverage percentage:', db.average_percentage(DATA_FILE))
