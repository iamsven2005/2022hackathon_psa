from tracker import db, login_manager
#hash generator tool: bcrypt
from tracker import bcrypt
#UserMixin module to help check whether the user is logged in or not
from flask_login import UserMixin

#logs the user in into their account from the login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    # creates the table columns and rows for the user credentials
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    #budget = db.Column(db.Integer(), nullable=False, default=1000)
    #important to include lazy=True in the relationship parameter!
    #items = db.relationship('Item', backref='owned_user', lazy=True)


    @property
    #defines the password as a property, everything else below this line are private variables that cannot be accessed outside of the User class
    def password(self):
        return self.password

    #sets password for the user account and hashes it
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    #checks the password hash integrity and also checks if the password matches the set password
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)




