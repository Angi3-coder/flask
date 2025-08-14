from flask import Flask, jsonify, request
from models import Students, db
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

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
@app.route('/students', methods=['GET', 'POST'])
def student():

    #GET
    if request.method == 'GET':
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

    #POST
    if request.method == ['POST']:
        #read the request body, convert it to python dictionary and stored in variable data
        data = request.get_json()

        #validate required fields
        if not data or not data.get('name') or not data.get('email') or not data.get('password'):
            return jsonify ({"error": "Missing fields"})

        #new instance of Students model is created using the values
        new_Student = Students(
            name = data['name'],
            email = data['email'],
            password = data["password"]
        )
        
        try:
            db.session.add(new_Student)
            db.session.commit()
            return jsonify({"message": "Student Created Successfully"}), 201
        except IntegrityError:
            db.session.rollback() #discard the pending changes
            return jsonify({'error': 'Email already exists'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500


#Student by ID
@app.route('/students/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def student_by_id(id):
    #GET STUDENT BY ID
    if request.method == ['GET']:
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
    
    #UPDATE
    if request.method == ['PUT']:
        #Retrieve student from the database
        student = Students.query.get(id)

        if not student:
            return({'error': 'Student not found'}), 404

        data = request.get_json()

        student.name = data.get('name', student.name)
        student.email= data.get('email', student.email)
        student.password = data.get('password', student.password)
        try:
            db.session.commit()
            return jsonify ({'message': "Student Updated Successfully"}), 200
        except IntegrityError:
            db.session.rollback()
            return jsonify ({'error': 'Email already exists'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
        
    #DELETE
    if request.method == ['DELETE']:
        student = Students.query.get(id)
        if not student:
            return jsonify({'error': 'Student not Found'}), 400
        
        db.session.delete(student)
        db.session.commit()

        return jsonify({'message': 'Student deleted successfully'}), 200


#app.run
if __name__ == '__main__':
    app.run(debug=True)