import pymysql
import pymysql.cursors
from fastapi import FastAPI, HTTPException, status


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
  
  return {'product': category}
