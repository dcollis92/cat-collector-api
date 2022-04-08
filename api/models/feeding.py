from datetime import datetime
from api.models.db import db

class Feeding(db.Model):
    __tablename__ = 'feedings'
    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column('meal', db.Enum('B', 'L', 'D', name='meal_type'))
    date = db.Column(db.DateTime, default=datetime.now(tz=None))
    created_at = db.Column(db.DateTime, default=datetime.now(tz=None))
    cat_id = db.Column(db.Integer, db.ForeignKey('cats.id'))

    def __repr__(self):
      return f"Feeding('{self.id}', '{self.meal}'"

    def serialize(self):
      return {
        "id": self.id,
        "meal": self.meal,
        "cat_id": self.cat_id,
        "date": self.date.strftime('%Y-%m-%d'),
      }

    def is_recent_meal(self):
      if self.date.strftime('%Y-%m-%d') == datetime.now(tz=None).strftime('%Y-%m-%d'):
        return True