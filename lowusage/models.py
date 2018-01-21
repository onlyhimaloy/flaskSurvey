from lowusage import db


class HOST(db.Model):
    __tablename__ = 'hostname'
    Hostname = db.Column('Hostname',db.Unicode,primary_key=True)
    Ml = db.Column('Ml',db.Integer)
    Server_Group = db.Column('Server_Group',db.Integer)
    Emp_name =db.Column('Emp_name',db.Integer)

class EMAIL(db.Model):
    __tablename__ = 'email'
    ID = db.Column('ID',db.Integer)
    ML = db.Column('ML',db.Unicode,primary_key=True)

class ANSWER(db.Model):
    __tablename__ = 'answer'
    Hostname = db.Column('Hostname',db.Unicode,primary_key=True)
    Ans1 = db.Column('Ans1',db.Unicode)
    Ans2 = db.Column('Ans2',db.Unicode)
    Ts = db.Column('Ts', db.Unicode)
    Emp_name = db.Column('Emp_name' , db.Unicode)
    Emp_dep = db.Column('Emp_dep' , db.Unicode)
    Emp_id = db.Column('Emp_id' , db.Unicode)

