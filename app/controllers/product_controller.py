from app.models.product import Product
from app.db.db_functions import DBFunctions


class ProductController:
    def __init__(self):
        self.dbcon = DBFunctions()

    def add_product(self, product_name, quantity, unit_price):
        # create a new product entry
        new_product = Product(product_name=product_name,
                              quantity=quantity, unit_price=unit_price)
        self.dbcon.add_new_product(product=new_product.product_name,
                                   quantity=new_product.quantity, unit_price=new_product.unit_price)
        return True

    def does_product_exist(self, product_name):
        # check if product exists.
        product_exists = self.dbcon.does_product_exist(product=product_name)
        if product_exists:
            return product_exists
        return False

    def update_product(self, product_name, quantity, unit_price, product_id):
        # update a product
        update = self.dbcon.update_product(
            product=product_name, quantity=quantity, unit_price=unit_price, product_id=product_id)
        if update:
            return True
        else:
            return False

    def get_single_product(self, product_id):
        # get single product
        product = self.dbcon.fetch_single_product(product_id=product_id)
        if product:
            return product
        return False

    def delete_product(self, product_id):
        # delete a product
        delete_item = self.dbcon.delete_product(product_id=product_id)
        if delete_item:
            return True
        return False

    def fetch_all_products(self):
        # fetch all available products
        available_products = self.dbcon.get_all_products()
        return available_products 
