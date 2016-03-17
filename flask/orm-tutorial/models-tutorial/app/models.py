from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(120))
    # You need to a relationship to Address table here
    # see http://flask-sqlalchemy.pocoo.org/2.1/models/#one-to-many-relationships

    def __repr__(self):
        return '<Customer %r>' % self.email

# Your Address code should go here
# class Address(db.Model):
