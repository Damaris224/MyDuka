from flask import Flask,render_template,request,redirect,url_for
from database import get_products,fetch_sales, insert_stock

#Flask instance
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products')
def products():
    products = get_products()
    return render_template('products.html',products =products)

@app.route('/add_products', methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['name']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        print ("Product added successfully")
        return redirect(url_for('products'))




@app.route('/sales')
def sales():
    sales = fetch_sales()
    return render_template('sales.html',sales = sales)


@app.route('/sales', methods=['GET', 'POST'])
def sales():
    if request.method == 'POST':
        pid = request.form['pid']
        quantity = request.form['quantity']
        insert_sale((pid, quantity))   # use your database function
        return redirect(url_for('sales'))  # reload page to show updated table

   
@app.route('/stock')
def stock():
    value = 789
    numbers = [1,2,3,4,5,6,7,8,9]
    return render_template('stock.html',x = value,y=numbers)

def stock(): 
    if request.method == 'POST': 
    pid = request.form['pid'] 
    stock_quantity = request.form['stock_quantity'] 
    insert_stock((pid, stock_quantity)) 
    return redirect(url_for('stock'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')




app.run(debug=True)




