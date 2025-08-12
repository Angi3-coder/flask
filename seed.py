#import app, db, models
from app import app
from models import Students, db


with app.app_context():
    #clear the database
    Students.query.delete()

    #add Students
    student1 = Students(name="Alice", email="a@gmail.com", password="alice123")
    student2 = Students(name="Bob", email="bob@gmail.com", password="bob12345")
    student3 = Students(name="Jane", email="jane@gmail.com", password="jane1235676")
    student4 = Students(name="John", email="john@gmail.com", password="john1234")
    student5 = Students(name="Charlie", email="charlie@gmail.com", password="Charlie123")


    newStudents = [student1, student2, student3, student4, student5]

    #add student to session
    db.session.add_all(newStudents)

    #commit session to database
    db.session.commit()

    print("Students added successfully")