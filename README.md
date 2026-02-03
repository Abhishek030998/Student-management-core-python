# Student Management (Core Python)

A small, file-based student management project in pure Python. It stores records in `students.csv`, calculates totals/percentages, and includes simple utilities like search and age calculation.

## Features
- Create a student with validated email and marks
- Generate sample data to a CSV file
- List top students above a percentage threshold
- Search students by name
- Remove students by ID
- Calculate a student's age from date of birth
- Compute average class percentage

## Project Structure
- `main.py` entry point and example usage
- `students/models.py` student data model
- `students/db.py` CSV persistence and queries
- `students/utils.py` helpers (validation, IDs, sample data)
- `students.csv` data store (auto-created if missing)

## Requirements
- Python 3.8+

## Run
```bash
python main.py
```

On first run, the app creates `students.csv` with sample data and prints:
- Top students with percentage > 80%
- Average percentage

## Use In Code
```python
from students import db, utils
from students.models import Student

DATA_FILE = "students.csv"

students = db.load_students(DATA_FILE)
print("Average:", db.average_percentage(DATA_FILE))

new_student = Student(
    id=utils.generate_id({s.id for s in students}),
    name="Alex Morgan",
    email="alex.morgan@example.com",
    eng=90,
    maths=88,
    science=92,
    dob="2004-06-15",
)
db.add_student(DATA_FILE, new_student)
```

## Interactive Functions
If you want to use the interactive helpers from `main.py`, you can import and call them:
```python
from main import createStudent, findStudentByName, removeStudent, age_of_student

createStudent()
findStudentByName()
removeStudent()
age_of_student()
```

## CSV Format
The CSV header is:
```
id,name,email,eng,maths,science,dob,total,percentage
```

## Notes
- Marks are expected to be integers between 0 and 100.
- Date of birth uses ISO format `YYYY-MM-DD`.
