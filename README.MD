# Flask sqlalchemy
Step 1: Create and activate virtual environment
```
    python3 -m venv venv
    source venv/bin/activate
```
step 2:
```
pip install flask flask-sqlalchemy
```
Store the libraries installed in a file called requirements.txt by running this code in the terminal
```
pip freeze > requirements.txt
```
## Initializing Migrate
Install flask migrate extension
```
pip install flask_migrate
```
In app.py set up migration engine after iporting flask_migrate
```
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

In the terminal we run 

```
flask db init
```
This will create a migration/ folder where alembic will store migration scripts

Create migration
```
flask db migrate -m "Creates Students Table"
```
Apply migration
```
flask db upgrade
```
