from flask import render_template, redirect, request
from app import app, models, db
from .forms import *


@app.route('/')
def index():
    return redirect('/customers')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        customer = models.Customer(
                            fname = form.fname.data,
                            lname = form.lname.data,
                            company = form.company.data,
                            email = form.email.data,
                            phone = form.phone.data,
                            addresses = [])
        address = models.Address(
                            street = form.street.data,
                            city = form.city.data,
                            state = form.state.data,
                            country = form.country.data,
                            zipcode = form.zipcode.data,
                            customer_id = customer.id)
        customer.addresses.append(address)
        db.session.add(customer)
        db.session.commit()
        return redirect('/customers')
    return render_template('create_customer.html', form=form)

@app.route('/customers')
def display_customer():
    customers = models.Customer.query.all()
    return render_template('customers.html',
                            customers=customers)

@app.route('/customer_detail/<customer_id>')
def display_customer_details(customer_id):
    customer = models.Customer.query\
                .filter(models.Customer.id == customer_id)\
                .first()
    addresses = db.session.query(models.Address)\
                .join(models.Customer)\
                .filter(models.Customer.id == customer_id)\
                .all()
    orders = db.session.query(models.Order)\
                .join(models.Customer, models.Order.customers)\
                .filter(models.Customer.id == customer_id)\
                .all()
    print addresses
    return render_template('customer_details.html',
                            customer = customer,
                            addresses = addresses,
                            orders = orders)

@app.route('/create_order', methods=['GET', 'POST'])
def create_order():
    form = OrderForm()
    if form.validate_on_submit():
        order = models.Order(
                            name = form.name.data,
                            cost = form.cost.data,
                            parts = form.parts.data,
                            customers = [])
        db.session.add(order)
        db.session.commit()
        return redirect('/orders')
    return render_template('create_order.html', form=form)

@app.route('/orders')
def display_order():
    orders = models.Order.query.all()
    order_customers = list()
    for order in orders:
        oc = dict()
        oc["order"] = order
        oc["customers"] = db.session.query(models.Customer)\
                    .join(models.Order, models.Customer.orders)\
                    .filter(models.Order.id == order.id).all()
        order_customers.append(oc)
    print order_customers
    return render_template('orders.html',
                            order_customers=order_customers)
