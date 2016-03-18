from app import app, models, db
print models.Customer.query.all()
print "\n\n"
print models.Address.query.all()
print "\n\n"
print models.Order.query.all()

print db.session.query(models.Address).join(models.Customer).filter(models.Customer.id == 1).all()
print models.Customer.query.filter(models.Customer.id == 1).first()
print db.session.query(models.Customer)\
            .join(models.Order, models.Customer.orders)\
            .filter(models.Order.id == 1).all()

print db.session.query(models.Order)\
            .join(models.Customer, models.Order.customers)\
            .all()
