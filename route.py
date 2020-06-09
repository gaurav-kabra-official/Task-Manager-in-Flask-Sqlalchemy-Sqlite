from app import app, db
# use below line if commit() gives error
# from model import db
from flask import render_template, redirect, url_for
from model import Task
import form
from datetime import datetime


#decorater to funct index 
# runs function index when you are at "localhost:5000/index"
# may add more than one decorator to a funct
@app.route('/')
@app.route('/index')
def index():
    #return 'Hello World!'
    # Jinja is to pass arguments to web pages.E.g. 'developer' here
    tasks = Task.query.all()
    return render_template('index.html', developer='Gaurav Kabra', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    formAdd = form.AddTask()
    if formAdd.validate_on_submit():
        #print('Task you just added', formAdd.task.data)
        t = Task(task=formAdd.task.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=formAdd)
    

@app.route('/delete/<int:task_id>', methods=['GET','POST'])
def delete(task_id):
    t = Task.query.get(task_id)
    formDel = form.DeleteTask()
    if t:
        db.session.delete(t)
        db.session.commit()
        return redirect(url_for('index'))
    
    else:
        # print on terminal
        print('Task not found!')
        return render_template('delete.html', form=formDel, task_id=task_id, task=t.task)