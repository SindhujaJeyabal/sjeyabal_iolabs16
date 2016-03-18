from app import db

orders = db.Table('orders',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
    db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'))
)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), unique=False)
    lname = db.Column(db.String(20), unique=False)
    company = db.Column(db.String(20), unique=False)
    email = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    addresses = db.relationship('Address',
        backref=db.backref('customer', lazy='joined'), lazy='dynamic')
    orders = db.relationship('Order', secondary = orders,
        backref=db.backref('customers', lazy='dynamic'))

    def __repr__(self):
        return 'Customer ' +  str(self.id) + " " + self.fname + " " + self.lname

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(20), unique=False)
    city = db.Column(db.String(20), unique=False)
    state = db.Column(db.String(20), unique=False)
    country = db.Column(db.String(20), unique=False)
    zipcode = db.Column(db.String(20), unique=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self):
        return 'Address ' +  str(self.id) + " " + self.street + " " \
        + str(self.customer.id)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False)
    cost = db.Column(db.Integer, unique=False)
    parts = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return 'Orders ' +  self.name + " " + str(self.id) + " " + str(self.cost)
