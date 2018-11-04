from app import app, db
from app.models import Classroom, Student

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Classroom': Classroom, 'Student': Student}
