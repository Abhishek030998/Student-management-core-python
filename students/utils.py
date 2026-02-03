import re
import random
from datetime import date, timedelta
from typing import Set

EMAIL_RE = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

def validate_email(email: str) -> bool:
    return bool(EMAIL_RE.match(email))


def generate_id(existing_ids: Set[str]) -> str:
    # Generates a unique ID like S1001
    while True:
        candidate = f"S{random.randint(1000, 9999)}"
        if candidate not in existing_ids:
            return candidate


def calculate_age(student) -> int:
    return student.age()


def random_date(start_year=1995, end_year=2015) -> str:
    start = date(start_year, 1, 1)
    end = date(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    d = start + timedelta(days=random_days)
    return d.isoformat()


def generate_sample_data(n: int, filename: str):
    """Generate n random students and save to filename."""
    first_names = ['Alex','Jordan','Taylor','Sam','Riley','Casey','Jamie','Morgan','Drew','Avery']
    last_names = ['Smith','Johnson','Brown','Lee','Garcia','Martinez','Davis','Lopez','Wilson','Anderson']

    existing_ids = set()
    lines = []
    header = 'id,name,email,eng,maths,science,dob,total,percentage\n'
    for _ in range(n):
        sid = generate_id(existing_ids)
        existing_ids.add(sid)
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = f"{name.lower().replace(' ', '.')}@example.com"
        eng = random.randint(40, 100)
        maths = random.randint(40, 100)
        science = random.randint(40, 100)
        dob = random_date()
        total = eng + maths + science
        perc = round((total / 300) * 100, 2)
        lines.append(f"{sid},{name},{email},{eng},{maths},{science},{dob},{total},{perc}\n")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(header)
        f.writelines(lines)

    return filename
