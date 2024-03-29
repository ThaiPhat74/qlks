from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = '^%^&$^T&*Y(*&*^&*^*(&&*$^4765876986764^&%&*%^%$&*^(*^*%*&^436'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:%s@localhost/QLKS_DATA?charset=utf8mb4' % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.config["PAGE_SIZE"] = 6

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

cloudinary.config(
    cloud_name="dapaiwg8m",
    api_key="148148595677726",
    api_secret="XesKx4E4iRvPgXk_0brt3XFHvpo"
)