# model class for a sale record
from app.models.product import Product

class Sale(Product):
    def __init__(self,product_name,quantity,unit_price,attendant,date):
        super(Sale, self).__init__(product_name, quantity, unit_price)
        self.attendant = attendant
        self.date = date