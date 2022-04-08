from datetime import datetime
from api.models.db import db

class Toy(db.Model):
    __tablename__ = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    color = db.Column(db.String(100))
    description = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    def __repr__(self):
      return f"Toy('{self.id}', '{self.name}'"

    def serialize(self):
      toy = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return toy