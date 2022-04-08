from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from api.models.db import db
from config import Config

# ============ Import Models ============
from api.models.user import User
from api.models.profile import Profile
from api.models.cat import Cat

# ============ Import Views ============
from api.views.auth import auth
from api.views.cats import cats
from api.models.toy import Toy


# Creates a new instances of CORS 
cors = CORS()
migrate = Migrate() 
# Allowable HTTP Methods
list = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE', 'LINK']

def create_app(config):
  app = Flask(__name__)
  app.config.from_object(config)

  db.init_app(app)
  migrate.init_app(app, db)
  # Configure cors instance with app and settings
  cors.init_app(app, supports_credentials=True, methods=list)

  # ============ Register Blueprints ============
  app.register_blueprint(auth, url_prefix='/api/auth') 
  app.register_blueprint(cats, url_prefix='/api/cats')

  return app

app = create_app(Config)