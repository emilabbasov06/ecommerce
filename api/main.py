import pymysql
import pymysql.cursors
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

# add DELETE and UPDATE methods for both Categories and Products

# Category
class Category(BaseModel):
  category_name: str

# Product
class Product(BaseModel):
  product_name: str
  content: str
  price: float
  date_added: str
  category: Optional[Category]


# Connect to Database
DB = pymysql.connect(
  host='localhost',
  user='root',
  password='admin_001',
  database='ecommerce',
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
)

# Create cursor to execute queries
cursor = DB.cursor()


def category(category_name):
  cursor.execute(f"SELECT * FROM categories WHERE category_name='{category_name}'")
  identified_category = cursor.fetchone()
  if identified_category:
    return identified_category.get('category_id')
  
  return -1


# Create the main pin-point for API
app = FastAPI()

@app.get('/products')
def get_products():
  cursor.execute('SELECT * FROM products')
  products = cursor.fetchall()
  return {'products': products}


@app.get('/products/{id}')
def get_product(id: int):
  cursor.execute(f'SELECT * FROM products WHERE product_id={id}')
  product = cursor.fetchone()
  
  if not product:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with {id} was not found!")
  
  return {'product': product}


@app.post('/products', status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
  CATEGORY_NAME = product.category.category_name
  CATEGORY_ID = category(CATEGORY_NAME)
  
  if CATEGORY_ID != -1:
    cursor.execute("""INSERT INTO products (product_name, content, price, date_added, category)
    VALUES (%s, %s, %s, %s, %s)""", (product.product_name, product.content, product.price, product.date_added, CATEGORY_ID))
    DB.commit()
    
    return {'message': 'New product added succesfully!'}
  
  return {'message': 'There was some technical problem'}


@app.delete('/products/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int):
  cursor.execute("""DELETE FROM products WHERE product_id = %s""", (str(id),))
  DB.commit()
  return {'message': 'Selected product was deleted succesfully!'}


@app.get('/categories')
def get_categories():
  cursor.execute('SELECT * FROM categories')
  categories = cursor.fetchall()
  return {'categories': categories}


@app.get('/categories/{id}')
def get_product(id: int):
  cursor.execute(f'SELECT * FROM categories WHERE category_id={id}')
  category = cursor.fetchone()
  
  if not category:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with {id} was not found!")
  
  return {'category': category}


@app.post('/categories', status_code=status.HTTP_201_CREATED)
def create_category(category: Category):
  cursor.execute("""INSERT INTO categories (category_name) VALUES(%s)""", (category.category_name))
  DB.commit()
  return {'message': 'New Category added to Database'}