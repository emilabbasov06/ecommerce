import pymysql
import pymysql.cursors
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from pymysql.err import InterfaceError

# Add User Authentication
# Work on design
# Make it a lot more secure


# Category
class Category(BaseModel):
  category_name: str

# Product
class Product(BaseModel):
  product_name: str
  content: str
  price: float
  category: Optional[Category]

# Order
class Order(BaseModel):
  order_name: str
  order_price: float

# LoginForm
class Login(BaseModel):
  email: EmailStr
  password: str

  
try:
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

  origins = [
    'http://localhost:5173',
  ]

  app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
  )
  
  @app.post('/check')
  def check_user(login: Login):
    EMAIL = login.email
    PASS = login.password
    
    print(EMAIL)
    print(PASS)
    
    result = cursor.execute(f'SELECT * FROM users WHERE email="{EMAIL}" AND password="{PASS}"')
    
    if result:
      return {'checked': True}
    
    return {'checked': False}
  

  @app.get('/products')
  def get_products():
    cursor.execute(f'SELECT * FROM products')
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
      cursor.execute("""INSERT INTO products (product_name, content, price, category)
      VALUES (%s, %s, %s, %s)""", (product.product_name, product.content, product.price, CATEGORY_ID))
      DB.commit()
      
      return {'message': 'New product added succesfully!'}
    
    return {'message': 'There was some technical problem'}


  @app.delete('/products/{id}', status_code=status.HTTP_204_NO_CONTENT)
  def delete_product(id: int):
    cursor.execute("""DELETE FROM products WHERE product_id = %s""", (str(id),))
    DB.commit()
    return {'message': 'Selected product was deleted succesfully!'}


  @app.put('/products/{id}')
  def update_product(id: int, product: Product):
    CATEGORY_ID = category(product.category.category_name)
    QUERY = (f'UPDATE products SET product_name="{product.product_name}", content="{product.content}", price={product.price}, category={CATEGORY_ID} WHERE product_id={str(id)}')
    
    cursor.execute(QUERY)
    DB.commit()
    
    return {'message': 'Product updated succesfully!'}


  # @app.put('/products/{id}')
  # def update_product(id: int, product: Product):
  #   cursor.execute("SELECT * FROM products WHERE product_id = ?", (str(id),))
  #   existing_product = cursor.fetchone()
  #   CATEGORY_NAME = product.category.category_name

  #   if not existing_product:
  #       DB.close()
  #       raise HTTPException(status_code=404, detail="Selected product was not found")

  #   # Update the product
  #   cursor.execute(
  #       """
  #       UPDATE products
  #       SET product_name = ?, content = ?, price = ?, date_added = ?, category = ?
  #       WHERE product_id = ?
  #       """,
  #       (product.product_name, product.content, product.price, product.date_added, category(CATEGORY_NAME), str(id))
  #   )

  #   DB.commit()
  #   DB.close()

  #   return {"message": "Selected product updated successfully"}


  @app.get('/categories')
  def get_categories():
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    return {'categories': categories}


  @app.get('/categories/{id}')
  def get_category(id: int):
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


  @app.delete('/categories/{id}', status_code=status.HTTP_204_NO_CONTENT)
  def delete_category(id: int):
    cursor.execute("""DELETE FROM categories WHERE category_id = %s""", (str(id),))
    DB.commit()
    return {'message': 'Selected category was deleted succesfully!'}


  @app.put('/categories/{id}')
  def update_category(id: int, category: Category):
    QUERY = (f'UPDATE categories SET category_name="{category.category_name}" WHERE category_id={str(id)}')
    cursor.execute(QUERY)
    DB.commit()
    return {'message': 'Category updated succesfully!'}


  @app.get('/orders')
  def get_orders():
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    return {'orders': orders}


  @app.post('/orders')
  def create_order(order: Order):
    cursor.execute("""INSERT INTO orders (order_name, order_price) VALUES(%s, %s)""", (order.order_name, order.order_price))
    DB.commit()
    return {
      'message': 'New order added succesfully!'
    }
except InterfaceError:
  print(InterfaceError)