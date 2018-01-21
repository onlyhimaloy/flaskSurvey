from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from sqlalchemy import func

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'top secret!123#098'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://lowusage:lowusage@1230@localhost/lowusage'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

import lowusage.views
