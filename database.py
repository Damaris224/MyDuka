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

#fetches sales from the database and returns them as a list of tuples
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
    
 
sale1 = (1, 2, 60000)
sale2 = (2, 1, 40000) 

insert_sale(sale1) 
insert_sale(sale2)

#profit per
#select p.name, (products.selling_price *sales.quantity)as total_sales from products
def sales_per_products():
    cur.execute("""SELECT products_name as p.name,sum(products.selling_price * sales.quantity) aS total_sales from products JOIN sales ON sales.pid = product.id group by (p_name)""")
    sales_per_product = cur.fetchall()
    return sales_per_product

sales_per_product = sales_per_products()
print(sales_per_product)

def get_profit_per_day():
    cur.execute("""
                select date(sales.created_at) as date ,sum((products.selling_price - products.buying_price) * sales.quantity) as profit from sales join products on products.id = sales.product_id group by date order by date;
                """)
    profit_per_day = cur.fetchall()
    return profit_per_day

profit_per_day = get_profit_per_day()
print(profit_per_day)
  #q1
  #insert stock data
def insert_stock(values):
    cur.execute("INSERT INTO stock (pid, quantity) VALUES (%s, %s)", values)
    conn.commit()
#fetch
def fetch_stock_data():
    cur.execute("SELECT * FROM stock")
    return cur.fetchall()

#sales per day
def get_sales_per_day():
    cur.execute("""
        SELECT DATE(sales.created_at) AS sale_date, 
               SUM(products.selling_price * sales.quantity) AS daily_revenue
        FROM sales 
        JOIN products ON products.id = sales.pid 
        GROUP BY sale_date 
        ORDER BY sale_date DESC;
    """)
    return cur.fetchall()

#profit per day
def get_profit_per_day():
    cur.execute("""
        SELECT DATE(sales.created_at) AS sale_date, 
               SUM((products.selling_price - products.buying_price) * sales.quantity) AS daily_profit
        FROM sales 
        JOIN products ON products.id = sales.pid 
        GROUP BY sale_date 
        ORDER BY sale_date DESC;
    """)
    return cur.fetchall()
   

