from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# __name__ == __main__ by default
app = Flask(__name__)
# for csrf
app.config['SECRET_KEY'] = 's-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

# This import must be after app has been instantiated
from route import *

if __name__ == '__main__':
    # debug=True ensures not to restart server every time you make changes
    app.run(debug=True)