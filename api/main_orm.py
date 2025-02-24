from fastapi import FastAPI, Depends, HTTPException, status

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from datetime import datetime

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

engine = create_engine('mysql://root:admin_001@localhost/ecommerce')
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

Base = declarative_base()


class UserModel(Base):
  __tablename__ = 'users'
  
  user_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  username = Column(String(255))
  email = Column(String(255), unique=True, nullable=False)
  password = Column(String(255), nullable=False)
  created_at = Column(DateTime, default=datetime.utcnow)


class CategoryModel(Base):
  __tablename__ = 'categories'

  category_id = Column(Integer, Sequence('category_id_seq'), primary_key=True)
  user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
  category_name = Column(String(255))
  created_at = Column(DateTime, default=datetime.utcnow)
  user = relationship('UserModel')


class ProductModel(Base):
  __tablename__ = 'products'

  product_id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
  user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
  category_id = Column(Integer, ForeignKey('categories.category_id'), nullable=False)
  product_name = Column(String(255))
  content = Column(String(255))
  price = Column(Float)
  created_at = Column(DateTime, default=datetime.utcnow)
  user = relationship('UserModel')
  category = relationship('CategoryModel')


class OrderModel(Base):
  __tablename__ = 'orders'
  
  order_id = Column(Integer, Sequence('order_id_seq'), primary_key=True)
  user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
  order_name = Column(String(255))
  order_price = Column(Float)
  created_at = Column(DateTime, default=datetime.utcnow)
  user = relationship('UserModel')
  

# Pydantic Models
class Login(BaseModel):
  email: EmailStr
  password: str


Base.metadata.create_all(engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

app = FastAPI()


origins = [
  'http://localhost:5173',
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # You can specify a list of allowed origins instead of "*"
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.post('/check')
def check(login: Login, db: Session = Depends(get_db)):
  EMAIL = login.email
  PASSWORD = login.password
  
  checked = db.query(UserModel).filter_by(email=EMAIL, password=PASSWORD).first()
  if checked:
    return {'checked': True}
  
  return {'checked': False}


@app.get('/categories')
def get_categories(db: Session = Depends(get_db)):
  categories = db.query(CategoryModel).all()
  if categories:
    return {'categories': categories}
  
  return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There was a problem!')

@app.get('/categories/{id}')
def get_category(id: int, db: Session = Depends(get_db)):
  category = db.query(CategoryModel).filter(CategoryModel.category_id == id).first()
  if category:
    return {'category': category}

  return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Category with id: {id} not found!')


@app.get('/products')
def get_products(db: Session = Depends(get_db)):
  products = db.query(ProductModel).all()
  if products:
    return {'products': products}

  return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There was a problem!')


@app.get('/products/{id}')
def get_product(id: int, db: Session = Depends(get_db)):
  product = db.query(ProductModel).filter(ProductModel.product_id == id).first()
  if product:
    return {'product': product}
  
  return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There was a problem!')


@app.get('/orders')
def get_orders(db: Session = Depends(get_db)):
  orders = db.query(OrderModel).all()
  if orders:
    return {'orders': orders}
  
  return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There was a problem!')


@app.get('/orders/{id}')
def get_order(id: int, db: Session = Depends(get_db)):
  order = db.query(OrderModel).filter(OrderModel.order_id == id).first()
  if order:
    return {'order': order}
  
  return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There was a problem!')