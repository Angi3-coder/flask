from flask import Flask, jsonify
from models import Students, db
from flask_migrate import Migrate

app = Flask(__name__)

#configure our app
#tell flask where our database is
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#disable track modification (recommended setting)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#INITIALIZE db with app
db.init_app(app)

#set-up migration engine
#Flask-migrate - flask library that works with alembic to keep track of our database changes
migrate = Migrate(app, db)

@app.route("/")
def home():
    return "Hello"

#GET Students
@app.route('/students')
def students():
    #query all students
    students = Students.query.all()

    #create a list to store the students
    students_list = []

    #convert each student to a dictionary
    for student in students:
        student_dict = {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'password': student.password,
            'course_id': student.course.id if student.course else None,
            'assignments': [
                {
                    'id': assignment.id,
                    'title': assignment.title
                } for assignment in student.assignments
            ]
        }
        students_list.append(student_dict)

    return jsonify(students_list)


#get student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    student = Students.query.get(id)

    if not student:
        return jsonify({'error': 'Student not found'}), 404

    student_data = {
        'id': student.id,
        'name': student.name,
        'email': student.email,
        'password': student.password,
        'course_id': student.course.id if student.course else None,
        'assignments': [
            {
                'id': assignment.id,
                'title': assignment.title
            } for assignment in student.assignments
        ]
    }
    return jsonify(student_data), 200


#app.run
if __name__ == '__main__':
    app.run(debug=True)