from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

#link to a database table
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tmkstyyzkczmxk:38aa0429f59ca322ba50b49b993a82dcf288bec4e54e7064ceb960231dca317f@ec2-3-217-14-181.compute-1.amazonaws.com:5432/deeij0oo06d2gg'
#important to include your secret key before running your app!
app.config['SECRET_KEY'] = 'u8x/A%D*G-KaPdSgVkYp3s6v9y$B&E(H'
#connect your app to your db
db = SQLAlchemy(app)
#to run the hash generator for your app
bcrypt = Bcrypt(app)
#login manager for your web app
login_manager = LoginManager(app)
#sqlalchemy db migrating tool
migrate = Migrate(app, db)
#redirects to user to login_page if not logged in
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from tracker import routes
