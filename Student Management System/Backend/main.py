from fastapi import FastAPI, HTTPException
import psycopg2
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],      # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],      # Allow all headers
)

connection = psycopg2.connect(os.getenv('DATABASE_URL'))

cursor = connection.cursor()

class Student(BaseModel):
    id: int = None
    name: str = None
    course: str = None
# Get All Students 

@app.get('/students')
def get_all_students():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    print()
    result = []
    for row in rows:
        result.append({
            'id' : row[0],
            'name' : row[1],
            'course' : row[2]
        })
    return result

@app.get('/students/{id}')
def get_single_students(id: int):
    try:
        cursor.execute('SELECT * FROM students WHERE id=%s', (id,))
        row = cursor.fetchone()
        return{
            'id' : row[0],
            'name' : row[1],
            'course' : row[2]
        }
    except Exception as e:
        raise HTTPException(status_code=404,detail='Student Record Not Found')

# Create Student record
@app.post('/students')
def create_student_record(student: Student):
    try:
        cursor.execute('INSERT INTO students VALUES(%s, %s, %s)',(student.id, student.name, student.course))
        connection.commit()
        return {
            'message': 'student Record Created Successfully'
        }
    except psycopg2.integrityError:
        connection.rollback()
        raise HTTPException(status_code=404, detail='Student Record Already Exists')

# UPdateStudent Record 
@app.put('/students/{id}')
def replace_student_record(id: int, student: Student):
    try:
        cursor.execute('UPDATE students SET id=%s, name=%s, course=%s WHERE id=%s',(student.id, student.name, student.course, id))
        connection.commit()
        return {
                'message': 'student Record Updated Successfully'
            }
    except Exception:
        raise HTTPException(status_code=404, detail='New Student Record Already Exists')

# Partialy Update Student Record 
@app.patch('/students/{id}')
def replace_student_record(id: int, student: Student):
    if(student.id != None):
        cursor.execute('UPDATE students SET id=%s WHERE id=%s',(student.id, id))
        connection.commit()
    if(student.name != None):
        cursor.execute('UPDATE students SET name=%s WHERE id=%s',(student.name, id))
        connection.commit()
    if(student.course != None):
        cursor.execute('UPDATE students SET course=%s WHERE id=%s',(student.course, id))
        connection.commit()
    return {
                'message': 'Partial Record Updated Successfully'
            }

@app.delete('/students/{id}')
def replace_student_record(id: int,):
    cursor.execute('DELETE FROM students WHERE id=%s',(id,))
    connection.commit()
    if(cursor.rowcount == 0):
        raise HTTPException(status_code=404, detail='Student ID Not Found')
    else:
        return {
                'message': 'student Record Deleted Successfully'
            }
