#import app, db, models
from app import app
from models import Students,Course, Assignments, db


with app.app_context():
    #clear the database
    Students.query.delete()
    Course.query.delete()
    Assignments.query.delete()

    #Courses
    course1 = Course(title= "Software Engineering")
    course2= Course(title="Cyber Security")
    course3= Course(title="Robotics")

    db.session.add_all([course1,course2,course3])
    db.session.commit()

    print("Course seeding successful")

    #Assignments
    assingnment1 = Assignments(title="Project 1")
    assingnment2 = Assignments(title="Project 2")
    assingnment3 = Assignments(title="Project 3")
    assingnment4 = Assignments(title="Project 4")
    assingnment5 = Assignments(title="Project 5")

    db.session.add_all([assingnment1, assingnment2, assingnment3, assingnment4, assingnment5])
    db.session.commit()
    print("Assignment seeding successful")

    #add Students
    student1 = Students(name="Alice", email="a@gmail.com", password="alice123", course_id = course1.id)
    student2 = Students(name="Bob", email="bob@gmail.com", password="bob12345", course_id = course2.id)
    student3 = Students(name="Jane", email="jane@gmail.com", password="jane1235676", course_id = course3.id)
    student4 = Students(name="John", email="john@gmail.com", password="john1234", course_id=course1.id)
    student5 = Students(name="Charlie", email="charlie@gmail.com", password="Charlie123", course_id = course2.id)

    ##assign assignments
    student1.assignments = [assingnment1,assingnment3]
    student2.assignments = [assingnment1, assingnment2, assingnment5]
    student3.assignments = [assingnment4, assingnment5]
    student4.assignments = [assingnment1, assingnment5, assingnment3]
    student5.assignments = [assingnment3, assingnment2, assingnment4]

    newStudents = [student1, student2, student3, student4, student5]

    #add student to session
    db.session.add_all(newStudents)

    #commit session to database
    db.session.commit()
    print("Students seeding successful")




    print("Seeding successfully")