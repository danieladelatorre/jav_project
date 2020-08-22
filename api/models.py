from . import db

class Information(db.Model):
    sl_no = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(50))
    ssc_p = db.Column(db.Float)
    ssc_b = db.Column(db.String(50))
    hsc_p = db.Column(db.Float)
    hsc_b = db.Column(db.String(50))
    hsc_s = db.Column(db.String(50))
    degree_p = db.Column(db.Float)
    degree_t = db.Column(db.String(50))
    workex = db.Column(db.String(50))
    etest_p = db.Column(db.Float)
    specialisation = db.Column(db.String(50))
    mba_p = db.Column(db.Float)
    status = db.Column(db.String(50))
    salary = db.Column(db.Integer)