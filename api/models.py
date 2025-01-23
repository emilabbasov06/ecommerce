from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(255), unique=True, nullable=False)

    # Define relationship with Product model
    products = relationship("Product", backref="category")

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    content = Column(String)
    price = Column(Float)
    date_added = Column(String(255)) 
    category_id = Column(Integer, ForeignKey('categories.category_id'))

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    order_name = Column(String(255))
    order_price = Column(Float)