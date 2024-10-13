from re import T
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from app import db

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)




Class Employer(db.Model):
    __tablename__ = 'employers'
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    #one to many with employees
    employees = relationship('Employee', backref=backref('employer'))

    #one to many with products
    products = relationship('Product', backref=backref('employer_too'))



Class Employee(db.Model):
    __tablename__ = 'employees'
    id = Column(Interger(), primary_key=True)
    name = Column(String())
    salary = Column(Interger())

    # one to many with products
    products = relationship('Product', backref=backref('employee_name'))

Class Products(db.Model):
    __tablename__ = 'products'
    id = Column(Interger(), primary_key=True)
    product_name = (String())
    product_price = (Interger())
    employer_id = Column(Integer(), ForeignKey('employers.id'))
    employee_id = Column(Integer(), ForeignKey('employees.id'))


