from app.db.db_manager import DBConnection

class DBFunctions:
    def __init__(self):
        self.connect = DBConnection()
        self.cursor = self.connect.dict_cursor

    def add_new_user(self, user_name, contact, role, password):
        #reegister a user
        query = (
            """INSERT INTO users (username, contact, role, password) VALUES ('{}', '{}', '{}', '{}')""".format(user_name, contact, role, password))
        self.cursor.execute(query)

    def is_username_exist(self,user_name):
        # check if username exists.
        query = ("""SELECT * FROM users where username = '{}'""".format(user_name))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        if user:
            return user
        return False    

    def is_contact_exist(self,contact):
        # check if user contact exists.
        query = ("""SELECT * FROM users where contact = '{}'""".format(contact))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        if user:
            return True
        return False        

    def user_login(self, user_name, password):
        #login a user
        query = ("""SELECT * from users where username = '{}' and password='{}'""".format(user_name, password))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        return user

    def add_new_product(self, product, quantity, unit_price):
        # add new product item
        query = (
            """INSERT INTO products (product, quantity, unit_price) VALUES ('{}', '{}', '{}')""".
            format(product, quantity, unit_price))
        self.cursor.execute(query)

    def does_product_exist(self,product):
        # check if product exists.
        query = ("""SELECT * FROM products where product = '{}'""".format(product))
        self.cursor.execute(query)
        product = self.cursor.fetchone()
        if product:
            return product
        return False

    def update_product(self, product, quantity, unit_price, product_id):
        #function to update product
        try:
            query = ("""UPDATE products SET product = '{}', quantity = '{}', unit_price = '{}' where product_id = '{}'""" .format(
                product, quantity, unit_price, product_id))
            self.cursor.execute(query)
            count = self.cursor.rowcount
            if int(count) > 0:
                return True
            else:
                return False   
        except:
            return False

    def fetch_single_product(self,product_id):
        # function to get details of a product
        self.cursor.execute("SELECT * FROM products WHERE product_id = '{}'" .format(product_id))
        row = self.cursor.fetchone()
        return row

    def delete_product(self, product_id):
        # function to delete a specific product
        query = ("""DELETE FROM products WHERE product_id = '{}'""" .format(product_id))
        self.cursor.execute(query)
        delete = self.cursor.rowcount
        if int(delete) > 0:
            return True
        else:
            return False

    def get_all_products(self):
        #function to get all added products
        self.cursor.execute("SELECT * from products")
        all_products = self.cursor.fetchall()
        return all_products

    def create_sale_record(self, product, quantity, amount, attendant, date):
        #create a sale record
        query = (
            """INSERT INTO sales (product, quantity, amount, attendant, date) VALUES ('{}', '{}', '{}', '{}', '{}')""".format(product, quantity, amount, attendant, date))
        self.cursor.execute(query)
    
    def get_newest_sale(self):
        #function to get the most recent sale record made
        self.cursor.execute("SELECT * FROM sales ORDER BY sale_id DESC LIMIT 1")
        newest_record = self.cursor.fetchall()
        return newest_record

    def get_all_sales(self):
        #function to get all available sales
        self.cursor.execute("SELECT * from sales")
        all_sales = self.cursor.fetchall()
        return all_sales

    def get_all_sales_for_user(self, user_name):
        #function to get all available sales
        self.cursor.execute("SELECT * FROM sales WHERE attendant = '{}'" .format(user_name))
        sale_record = self.cursor.fetchall()
        return sale_record 