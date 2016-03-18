# Models Lab/Homework
The goal for this lab is to get you comfortable translating your database models into actual code. We will be using [ORMs](https://en.wikipedia.org/wiki/Object-relational_mapping) to help us. The particular ORM that we will be using is SQLAlchemy (the flask implementation is called [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)).

We'll walk through the example together in class which will give you an idea of how this all works together. Your goal for this lab and homework is to create the remaining models, forms, and routes to complete v2 of the exercise from last week.

This means that you must:  
* Create the following tables and the appropriate relationships:
  * customer
  * address
  * order
  * Remember to run update_database.py whenever you make changes to any models.
    * This will update the database with your changes. However, **it will delete any data in the database**.
* Create the forms, templates, routes, etc necessary to input this data into the database.
* Create a view to showcase the data into your database (see the current implementation of "home.html" for example)

The following documentation will help answer any questions you may have.

## Helpful Documentation
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
- [Accessing SQLite3 Command Shell](https://www.sqlite.org/cli.html)
- [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/) (flask plugin for creating forms easily)
