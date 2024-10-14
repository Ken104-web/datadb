from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)




class Employer(db.Model):
    __tablename__ = 'employers'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    #one to many with employees
    employees = db.relationship('Employee', backref='employer')

    #one to many with products
    products = db.relationship('Product', backref='employer_too')



class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    salary = db.Column(db.Integer())

    # one to many with products
    products = db.relationship('Product', backref='employee_name')

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer(), primary_key=True)
    product_name = db.Column(db.String())
    product_price = db.Column(db.Integer())
    employer_id = db.Column(db.Integer(), db.ForeignKey('employers.id'))
    employee_id = db.Column(db.Integer(), db.ForeignKey('employees.id'))


