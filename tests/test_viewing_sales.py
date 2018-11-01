from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestViewingSale(BaseTestCase):
    
    def test_viewing_sales(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product_id="1", quantity="10",unit_price="200"),)   
                                )                      
            response2 = self.app.get("/api/v2/sales",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),)                 
            self.assertEqual(response2.status_code, 200)

    def test_viewing_attendant_sales(self):
            admin_login= self.admin_login()
            attendant_login = self.attendant_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+attendant_login['token']),
                                    data=json.dumps(dict(product_id="1", quantity="10",unit_price="200"),)   
                                )                      
            response2 = self.app.get("/api/v2/sales",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+attendant_login['token']),)                 
            self.assertEqual(response2.status_code, 200)

    def test_viewing_nonexisting_sales(self):
            admin_login= self.admin_login()
            attendant_login = self.attendant_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales/1",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="10",unit_price="200"),)   
                                )                      
            response2 = self.app.get("/api/v2/sales",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+attendant_login['token']),)                 
            reply = json.loads(response2.data.decode())
            self.assertEqual(reply.get("message"), "no sles recorded yet")
            self.assertEqual(response2.status_code, 404)

    def test_viewing_single_nonexisting_sale(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales/1",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="10",unit_price="200"),)   
                                )                      
            response2 = self.app.get("/api/v2/sales/2",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),)                 
            reply = json.loads(response2.data.decode())
            self.assertEqual(reply.get("message"), "sale record not added yet")
            self.assertEqual(response2.status_code, 404)

    def test_viewing_single_sale_impromper_id(self):
            admin_login= self.admin_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales/1",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="10",unit_price="200"),)   
                                )                      
            response2 = self.app.get("/api/v2/sales/a",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),)                 
            reply = json.loads(response2.data.decode())
            self.assertEqual(reply.get("message"), "Input should be an interger")
            self.assertEqual(response2.status_code, 400)

    def test_viewing_attendant_single_sale(self):
            admin_login= self.admin_login()
            attendant_login = self.attendant_login()
            response = self.app.post("/api/v2/products",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                    data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                                )
            response = self.app.post("/api/v2/sales",
                                    content_type='application/json', headers=dict(Authorization='Bearer '+attendant_login['token']),
                                    data=json.dumps(dict(product_id="1", quantity="10",unit_price="200"),)   
                                )                      
            response2 = self.app.get("/api/v2/sales/1",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+attendant_login['token']),)                 
            self.assertEqual(response2.status_code, 200)                                
