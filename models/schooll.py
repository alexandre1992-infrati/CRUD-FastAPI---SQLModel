from typing import Optional
from sqlmodel import Field, SQLModel


class SchoolModel(SQLModel, table=True):
    __tablename__: str = 'alunos'
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    grade: str
    note: float
    