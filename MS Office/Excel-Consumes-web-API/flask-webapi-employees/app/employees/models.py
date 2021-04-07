from app import db


class EmpMaster(db.Model):
    __tablename__ = 'employees'

    EMP_ID = db.Column(db.Integer, primary_key=True, autoincrement=False)
    FIRST_NAME = db.Column(db.String)
    LAST_NAME = db.Column(db.String)
    GENDER = db.Column(db.String(10))
    AGE = db.Column(db.Integer)
    EMAIL = db.Column(db.String(50))
    PHONE_NR = db.Column(db.String(20))
    EDUCATION = db.Column(db.String(20))
    MARITAL_STAT = db.Column(db.String(20))
    NR_OF_CHILDREN = db.Column(db.Integer)

    def __repr__(self):
        return '<Employee %r>' % self.EMP_ID
