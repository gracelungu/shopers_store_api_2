from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestViewingProducts(BaseTestCase):

    def test_viewing_nonexistant_products(self):
        admin_login= self.admin_login()
        response2 = self.app.get("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "no products added yet")                
        self.assertEqual(response2.status_code, 404)

    def test_viewing_nonexistant_product(self):
        admin_login= self.admin_login()
        response2 = self.app.get("/api/v2/products/1",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "product not added yet")                
        self.assertEqual(response2.status_code, 404)    
    
    def test_viewing_available_products(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                             )
        response2 = self.app.get("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),)                 
        self.assertEqual(response2.status_code, 200)

    def test_viewing_single_product(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                             )
        response2 = self.app.get("/api/v2/products/1",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),)                 
        self.assertEqual(response2.status_code, 200)

    def test_viewing_single_product_with_wrong_id(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                             )
        response2 = self.app.get("/api/v2/products/r",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "Input should be an interger")                  
        self.assertEqual(response2.status_code, 400)        