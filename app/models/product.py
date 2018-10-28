# model class for a product

class Product(object):
    def __init__(self, product_name, quantity, unit_price):
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price