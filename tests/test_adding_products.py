from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestProducts(BaseTestCase):

    def test_adding_product_successfully(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                             ) 
        reply = json.loads(response.data.decode())
        self.assertIn(("Life Jackets"), reply.get("product").values())
        self.assertEqual(response.status_code, 201)

    def test_adding_product_existing_product(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                             )
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                             )                      
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "product already exits, so its quantity has been updated")
        self.assertEqual(response.status_code, 200)
    
    def test_adding_product_no_product(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="", quantity="20",unit_price="200"),)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "product name is missing")
        self.assertEqual(response.status_code, 400)

    def test_adding_product_no_product_2(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product=" ", quantity="20",unit_price="200"),)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "product name is missing")
        self.assertEqual(response.status_code, 400)

    def test_adding_product_wrong_product(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product=" shirts", quantity="20",unit_price="200"),)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "product name must have no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_adding_product_wrong_quantity(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="shirts", quantity="qqq",unit_price="200"),)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "quantity must be only digits and must have no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_adding_product_no_quantity(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="shirts", quantity="",unit_price="200"),)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "quantity is missing")
        self.assertEqual(response.status_code, 400)

    def test_adding_product_zero_quantity(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="shirts", quantity="0",unit_price="200"),)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "quantity should be at least 1 item")
        self.assertEqual(response.status_code, 400)        

    def test_adding_product_wrong_price(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="shirts", quantity="200",unit_price=" xx"),)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "price must be only digits and must have no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_adding_product_zero_price(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="shirts", quantity="200",unit_price="0"),)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "unit price should be greater than zero")
        self.assertEqual(response.status_code, 400)    

    def test_adding_product_short_product(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="shi", quantity="200",unit_price="200"),)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "product name should be more than 4 characters long")
        self.assertEqual(response.status_code, 400)
        
                        