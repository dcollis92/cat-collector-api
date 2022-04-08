from datetime import datetime
from api.models.db import db

class Cat(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    breed = db.Column(db.String(100))
    description = db.Column(db.String(250))
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    def __repr__(self):
      return f"Cat('{self.id}', '{self.name}'"

    def serialize(self):
      cat = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return cat