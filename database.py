#conncets python and interacts with psql
import psychopg2 

conn = psychopg2.connect(
    host="localhost",#runs locally
    port = '5432',#default psql port
    user="postgres",
    password="Wangari@2004",
    dbname='myduka_db')

cur = conn.cursor()#fetches results from the database

cur.execute("select * from products")
products = cur.fetchall()
print(products)

def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data

data = get_data('sales')
print(data)

#fetches products from the database and returns them as a list of tuples
def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = get_products()
print(products)

#inserts new product into the products table
def insert_products(values):
    cur.execute("insert into products (name,buying_price,selling_price,quantity) values {values}")
    conn.commit()

#adds two products into the products table
product1 = ('samsung',20000,30000)
product2 = ('hp',30000,40000)

insert_products(product1)
insert_products(product2)

def get_sales(): 
    cur.execute("SELECT * FROM sales") 
    sales = cur.fetchall() 
    return sales
 
sales = get_sales() 
print(sales) 

# 2. Insert a new sale 
def insert_sale(values): 
    cur.execute("INSERT INTO sales(product_id, quantity, total_amount) VALUES %s", (values,)) 
    conn.commit() 
    
# Example sales data (assuming product_id exists in products table) 
sale1 = (1, 2, 60000) # product_id=1, quantity=2, total_amount=60000
sale2 = (2, 1, 40000) # product_id=2, quantity=1, total_amount=40000

insert_sale(sale1) 
insert_sale(sale2)