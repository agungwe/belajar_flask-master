from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# bagian upload file
UPLOAD_FOLDER = 'D:\\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#seeder
seeder = FlaskSeeder()
seeder.init_app(app,db)

#model
from app.model import todo, user

#routes
from app.route import routes, routeUser, routeTodo, uploadFile