from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

@dataclass
class Student:
    id: str
    name: str
    email: str
    eng: int
    maths: int
    science: int
    dob: str  # ISO format: YYYY-MM-DD
    total: Optional[int] = None
    percentage: Optional[float] = None

    def __post_init__(self):
        # Ensure marks are ints
        self.eng = int(self.eng)
        self.maths = int(self.maths)
        self.science = int(self.science)
        self.total = self.eng + self.maths + self.science
        self.percentage = round((self.total / 300) * 100, 2)

    def to_csv(self) -> str:
        return f"{self.id},{self.name},{self.email},{self.eng},{self.maths},{self.science},{self.dob},{self.total},{self.percentage}\n"

    @staticmethod
    def from_csv(line: str):
        parts = [p.strip() for p in line.split(',')]
        # id,name,email,eng,maths,science,dob,total,percentage
        return Student(
            id=parts[0],
            name=parts[1],
            email=parts[2],
            eng=int(parts[3]),
            maths=int(parts[4]),
            science=int(parts[5]),
            dob=parts[6],
            total=int(float(parts[7])) if parts[7] else None,
            percentage=float(parts[8]) if parts[8] else None,
        )

    def age(self) -> int:
        """Calculate age as of today."""
        dob_dt = datetime.strptime(self.dob, '%Y-%m-%d').date()
        today = datetime.today().date()
        age = today.year - dob_dt.year - ((today.month, today.day) < (dob_dt.month, dob_dt.day))
        return age
