from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from app import db

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

Class Employer(db.Model):
    __tablename__ = 'employers'
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    #one to many with employees
    employees = relationship('Employee', backref='employer')

    

db = SQLAlchemy(metadata=metadata)

