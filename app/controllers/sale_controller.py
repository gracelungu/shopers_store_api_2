from app.db.db_functions import DBFunctions
from app.models.sale import Sale


class SaleController:
    def __init__(self):
        self.dbcon = DBFunctions()

    def add_sale_record(self, product_id, quantity, attendant, date):
        # creating a sales record
        item = self.dbcon.fetch_single_product(product_id=product_id)
        if item:
            product = item["product"]
            _quantity = int(quantity)
            amount = (item["unit_price"]*int(quantity))
            _attendant = attendant
            _date = date
            new_sale = Sale(product_name=product, quantity=_quantity,
                            unit_price=amount, attendant=_attendant, date=_date)
            self.dbcon.create_sale_record(product=new_sale.product_name, quantity=new_sale.quantity,
                                          amount=new_sale.unit_price, attendant=new_sale.attendant, date=new_sale.date)
            new_quantity = int(item["quantity"])- _quantity
            self.dbcon.update_product(product=product, quantity=new_quantity, unit_price=item["unit_price"], product_id=product_id)
            return True
        else:
            return False
    def fetch_newest_sale(self):
        pass        
