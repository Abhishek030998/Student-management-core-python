from .models import Student
from typing import List
from functools import reduce

HEADER = 'id,name,email,eng,maths,science,dob,total,percentage\n'


def load_students(filename: str) -> List[Student]:
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return students
    if not lines:
        return students
    for line in lines[1:]:  # skip header
        if line.strip():
            students.append(Student.from_csv(line))
    return students


def save_students(filename: str, students: List[Student]):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(HEADER)
        for s in students:
            f.write(s.to_csv())


def add_student(filename: str, student: Student):
    students = load_students(filename)
    students.append(student)
    save_students(filename, students)


def remove_student_by_id(filename: str, sid: str) -> bool:
    students = load_students(filename)
    new_students = [s for s in students if s.id != sid]
    if len(new_students) == len(students):
        return False
    save_students(filename, new_students)
    return True


def find_by_name(filename: str, name_query: str) -> List[Student]:
    students = load_students(filename)
    q = name_query.lower()
    return [s for s in students if q in s.name.lower()]


def students_above_percentage(filename: str, threshold: float) -> List[Student]:
    students = load_students(filename)
    return list(filter(lambda s: s.percentage is not None and s.percentage > threshold, students))


def average_percentage(filename: str) -> float:
    students = load_students(filename)
    if not students:
        return 0.0
    total = reduce(lambda acc, s: acc + (s.percentage or 0), students, 0)
    return round(total / len(students), 2)
