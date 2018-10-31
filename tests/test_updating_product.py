from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestUpdatingProducts(BaseTestCase):
    
    def test_updating_nonexistant_product(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.put("/api/v2/products/2",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="200",unit_price="200"),)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "product not updated or doesn't exist")
            self.assertEqual(response.status_code, 400)

    def test_updating_product(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.put("/api/v2/products/1",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="200",unit_price="200"),)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "product successfully updated.")
            self.assertEqual(response.status_code, 200)

    def test_updating_product_impromper_id(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.put("/api/v2/products/a",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="200",unit_price="200"),)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "Input should be an interger")
            self.assertEqual(response.status_code, 400)

    def test_updating_product_wrong_product(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.put("/api/v2/products/1",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product=" ", quantity="200",unit_price="200"),)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "product name is missing")
            self.assertEqual(response.status_code, 400)

    def test_updating_product_missing_keys(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.put("/api/v2/products/1",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(quantity="200",unit_price="200"),)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "a 'key(s)' is missing in your request body")
            self.assertEqual(response.status_code, 400)                                