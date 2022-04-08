from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.toy import Toy

toys = Blueprint('toys', 'toys')

@toys.route('/', methods=["POST"]) 
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]

  toy = Toy(**data)
  db.session.add(toy)
  db.session.commit()
  return jsonify(toy.serialize()), 201