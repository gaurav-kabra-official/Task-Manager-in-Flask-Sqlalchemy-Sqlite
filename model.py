from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(300), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '{task} added on {date}'.format(task=self.task, date=self.date)
        