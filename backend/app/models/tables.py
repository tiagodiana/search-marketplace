from app import db
from sqlalchemy import func


class Researches(db.Model):
    __table__ = 'researches'
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(40))
    site = db.Column(db.String(40))
    type = db.Column(db.String(40))
    query = db.Column(db.String(40))
    result = db.Column(db.Text)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return '<Result %r>' % self.result

