from app.db.db_functions import DBFunctions
from app.models.sale import Sale


class SaleController:
    def __init__(self):
        self.dbcon = DBFunctions()

    def add_sale_record(self, product_id, quantity, attendant, date):
        # creating a sales record
        item = self.dbcon.fetch_single_product(product_id=product_id)
        if item:
            if item["quantity"] > int(quantity):
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
        return False        

    def fetch_all_sales(self):
        # fetch all available sale records
        all_sales = self.dbcon.get_all_sales()
        return all_sales

    def fetch_all_sales_for_user(self, user_name):
        # fetch all available sale records for a particular user
        all_sales = self.dbcon.get_all_sales_for_user(user_name=user_name)
        return all_sales
    
    def fetch_single_sale(self, sale_id):
        # fetch a sale record
        sale_record = self.dbcon.get_single_sale(sale_id=sale_id)
        return sale_record

    def fetch_single_sale_for_user(self, sale_id, user_name):
        # fetch a sale record for a particular user
        sale_record = self.dbcon.get_single_sale_for_user(sale_id=sale_id, user_name=user_name)
        return sale_record  
