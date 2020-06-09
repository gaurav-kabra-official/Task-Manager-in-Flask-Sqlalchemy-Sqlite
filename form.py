from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTask(FlaskForm):
    # validate that string not empty
    task = StringField('Task...', validators=[DataRequired()])
    submit = SubmitField('+ Add Task')

class DeleteTask(FlaskForm):
    submit = SubmitField('- Delete Task')