from app.db.db_manager import DBConnection

connect = DBConnection()
cursor = connect.dict_cursor

class DBFunctions:

    def add_new_user(self, user_name, contact, role, password):
        #reegister a user
        query = (
            """INSERT INTO users (username, contact, role, password) VALUES ('{}', '{}', '{}', '{}')""".format(user_name, contact, role, password))
        cursor.execute(query)

    def is_username_exist(self,user_name):
        # check if username exists.
        query = ("""SELECT * FROM users where username = '{}'""".format(user_name))
        cursor.execute(query)
        user =cursor.fetchone()
        if user:
            return user
        return False    

    def is_contact_exist(self,contact):
        # check if user contact exists.
        query = ("""SELECT * FROM users where contact = '{}'""".format(contact))
        cursor.execute(query)
        user =cursor.fetchone()
        if user:
            return True
        return False        

    def user_login(self, user_name, password):
        #login a user
        query = ("""SELECT * from users where username = '{}' and password='{}'""".format(user_name, password))
        cursor.execute(query)
        user =cursor.fetchone()
        return user

    def add_new_product(self, product, quantity, unit_price):
        # add new product item
        query = (
            """INSERT INTO products (product, quantity, unit_price) VALUES ('{}', '{}', '{}')""".
            format(product, quantity, unit_price))
        cursor.execute(query)

    def does_product_exist(self,product):
        # check if product exists.
        query = ("""SELECT * FROM products where product = '{}'""".format(product))
        cursor.execute(query)
        product = cursor.fetchone()
        if product:
            return product
        return False

    def update_product(self, product, quantity, unit_price, product_id):
        #function to update product
        try:
            query = ("""UPDATE products SET product = '{}', quantity = '{}', unit_price = '{}' where product_id = '{}'""" .format(
                product, quantity, unit_price, product_id))
            cursor.execute(query)
            count = cursor.rowcount
            if int(count) > 0:
                return True
            else:
                return False   
        except:
            return False

    def fetch_single_product(self,product_id):
        # function to get details of a product
        cursor.execute("SELECT * FROM products WHERE product_id = '{}'" .format(product_id))
        row = cursor.fetchone()
        return row

    def delete_product(self, product_id):
        # function to delete a specific product
        query = ("""DELETE FROM products WHERE product_id = '{}'""" .format(product_id))
        cursor.execute(query)
        delete = cursor.rowcount
        if int(delete) > 0:
            return True
        else:
            return False

    def get_all_products(self):
        #function to get all added products
        cursor.execute("SELECT * from products")
        all_products = cursor.fetchall()
        return all_products

    def create_sale_record(self, product, quantity, amount, attendant, date):
        #create a sale record
        query = (
            """INSERT INTO sales (product, quantity, amount, attendant, date) VALUES ('{}', '{}', '{}', '{}', '{}')""".format(product, quantity, amount, attendant, date))
        cursor.execute(query)
    
    def get_newest_sale(self):
        #function to get the most recent sale record made
        cursor.execute("SELECT * FROM sales ORDER BY sale_id DESC LIMIT 1")
        newest_record = cursor.fetchall()
        return newest_record

    def get_all_sales(self):
        #function to get all available sales
        cursor.execute("SELECT * from sales")
        all_sales = cursor.fetchall()
        return all_sales

    def get_all_sales_for_user(self, user_name):
        #function to get all available sales
        cursor.execute("SELECT * FROM sales WHERE attendant = '{}'" .format(user_name))
        sale_record = cursor.fetchall()
        return sale_record

    def get_single_sale(self, sale_id):
        #function to get the most recent sale record made
        cursor.execute("SELECT * FROM sales WHERE sale_id = '{}'" .format(sale_id))
        sale_record = cursor.fetchall()
        return sale_record

    def get_single_sale_for_user(self, sale_id, user_name):
        #function to get the most recent sale record made
        cursor.execute("SELECT * FROM sales WHERE sale_id = '{}' AND attendant = '{}'" .format(sale_id, user_name))
        sale_record = cursor.fetchall()
        return sale_record 