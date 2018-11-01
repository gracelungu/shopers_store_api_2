from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestCreatingSale(BaseTestCase):
    
    def test_selling_nonexisting_product(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product_id="2", quantity="30",unit_price="200"),)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "sale record not added. Product not available or is at minimum quantity")
            self.assertEqual(response.status_code, 400)

    def test_selling_product(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product_id="1", quantity="10",unit_price="200"),)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "sale record successfully added")
            self.assertEqual(response.status_code, 201)

    def test_selling_more_product(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product_id="1", quantity="30",unit_price="200"),)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "sale record not added. Product not available or is at minimum quantity")
            self.assertEqual(response.status_code, 400)        

    def test_selling_product_impromper_id(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product_id="q", quantity="10",unit_price="200"),)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "Input should be an interger")
            self.assertEqual(response.status_code, 400)

    def test_selling_product_impromper_quantity(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product_id="1", quantity="q",unit_price="200"),)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "Input should be an interger")
            self.assertEqual(response.status_code, 400)                        
