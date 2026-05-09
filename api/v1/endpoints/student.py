from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from models.schooll import SchoolModel
from core.dependency import get_session
from sqlmodel.sql.expression import Select, SelectOfScalar


#Bypass - Warning SQLModel
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


router = APIRouter()


#Método POST
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=SchoolModel)
async def post_student(schooll: SchoolModel, db: AsyncSession = Depends(get_session)):
    new_student = SchoolModel(
        name=schooll.name,
        age=schooll.age,
        grade=schooll.grade,
        note=schooll.note
    )
    db.add(new_student)
    await db.commit()
    return new_student


#Método GET - Alunos
@router.get('/', response_model=List[SchoolModel])
async def get_students(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(SchoolModel)
        results = await session.execute(query)
        students: List[SchoolModel] = results.scalars().all()
        return students
    

#Método GET - Aluno
@router.get('/{student_id}', response_model=SchoolModel, status_code=status.HTTP_200_OK)
async def get_student(student_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(SchoolModel).filter(SchoolModel.student_id == student_id)
        result = await session.execute(query)
        student: SchoolModel = result.scalar_one_or_none()
        if student:
            return student
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        else:
            raise HTTPException(detail='Aluno não localizado', status_code=status.HTTP_404_NOT_FOUND)


#Método PUT
@router.put('/{student_id}', status_code=status.HTTP_202_ACCEPTED, response_model=SchoolModel)
async def put_student(student_id: int, schooll:SchoolModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(SchoolModel).filter(SchoolModel.student_id == student_id)
        result = await session.execute(query)
        student_update: SchoolModel = result.scalar_one_or_none()
        if student_update:
            student_update.name = schooll.name
            student_update.age = schooll.age
            student_update.grade = schooll.grade
            student_update.note = schooll.note
            await session.commit()
            return student_update
        else:
            raise HTTPException(detail='Aluno não localizado', status_code=status.HTTP_404_NOT_FOUND)


#Método DELETE
@router.delete('/{student_id}', status_code=status.HTTP_204_NO_CONTENT)
async def student_del(student_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(SchoolModel).filter(SchoolModel.student_id == student_id)
        result = await session.execute(query)
        student_delete: SchoolModel = result.scalar_one_or_none()
        if student_delete:
            await session.delete(student_delete)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Aluno não localizado', status_code=status.HTTP_404_NOT_FOUND)