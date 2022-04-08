from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.cat import Cat

cats = Blueprint('cats', 'cats')

@cats.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  cat = Cat(**data)
  db.session.add(cat)
  db.session.commit()
  return jsonify(cat.serialize()), 201

@cats.route('/', methods=["GET"])
def index():
  cats = Cat.query.all()
  return jsonify([cat.serialize() for cat in cats]), 200

@cats.route('/<id>', methods=["GET"])
def show(id):
  cat = Cat.query.filter_by(id=id).first()
  cat_data = cat.serialize()
  return jsonify(cat=cat_data), 200

@cats.route('/<id>', methods=["PUT"]) 
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  cat = Cat.query.filter_by(id=id).first()

  if cat.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(cat, key, data[key])

  db.session.commit()
  return jsonify(cat.serialize()), 200