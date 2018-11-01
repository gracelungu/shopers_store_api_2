from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class Test_auth(BaseTestCase):

    def test_registration_success(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "Attendant account created")
        self.assertEqual(response.status_code, 201)

    def test_registration_with_short_username(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="ara", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username should be more than 4 characters long")
        self.assertEqual(response.status_code, 400)    

    def test_registration_with_missing_keys(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict( contact="0700-000000", role="attendant", password="araali"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "a 'key(s)' is missing in your registration body")
        self.assertEqual(response.status_code, 400)    

    def test_registration_with_wrong_username(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="", contact="0700-000000", role="attendant", password="araali"),)
                                 )                       
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "usename is missing")
        self.assertEqual(response.status_code, 400)

    def test_registration_with_no_username(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name=" ", contact="0700-000000", role="attendant", password="araali"),)
                                 )                       
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username is missing")
        self.assertEqual(response.status_code, 400)     
    
    def test_registration_with_existing_username(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        response2 = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )                         
        reply = json.loads(response2.data)
        self.assertEqual(reply.get("message"), "username exists")
        self.assertEqual(response2.status_code, 409)

    def test_registration_with_existing_contact(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        response2 = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali24", contact="0700-000000", role="attendant", password="araali"),)
                                 )                         
        reply = json.loads(response2.data)
        self.assertEqual(reply.get("message"), "contact exists")
        self.assertEqual(response2.status_code, 409)    

    def test_registration_with_wrong_contact(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="07000000000", role="attendant", password="araali"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "contact format must be [07xx-xxxxxx],in digits with no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_registration_with_wrong_role(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attend", password="araali"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "role should either be admin or attendant")
        self.assertEqual(response.status_code, 400)

    def test_registration_with_impromper_username(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="   araali2", contact="0700-000000", role="admin", password="araali"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username must have no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_registration_with_no_password(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="admin", password=""),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "password is missing")
        self.assertEqual(response.status_code, 400)            

    def test_user_login_successful(self):
        """ Test for successful login """
        self.register_attendant()
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(user_name="araali", password="araali"))
        )
        self.assertEqual(response.status_code, 200)

    def test_user_login_unsuccessful(self):
        """ Test for successful login """
        self.register_attendant()
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali", password="araali"))
        )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "a 'key(s)' is missing in login body")
        self.assertEqual(response.status_code, 400)
    
    def test_user_login_with_wrong_username(self):
        """ Test for successful login """
        self.register_attendant()
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(user_name=" araali", password="araali"))
        )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "wrong login credentials or user does not exist")
        self.assertEqual(response.status_code, 400)

    def test_user_login_with_wrong_username_2(self):
        """ Test for successful login """
        self.register_attendant()
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(user_name="", password="araali"))
        )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username is missing")
        self.assertEqual(response.status_code, 400)

    def test_user_login_with_no_password(self):
        """ Test for successful login """
        self.register_attendant()
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(user_name="araali", password=""))
        )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "password is missing")
        self.assertEqual(response.status_code, 400)

    def test_user_update_success(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        response = self.app.put("/api/auth/users",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="admin", password="araali"),)
                                 )                         
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "user role succesfully updated")
        self.assertEqual(response.status_code, 200)

    def test_user_update_with_wrong_username(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        response = self.app.put("/api/auth/users",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name=" ", contact="0700-000000", role="admin", password="araali"),)
                                 )                         
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username is missing")
        self.assertEqual(response.status_code, 400)

    def test_user_update_with_no_user(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        response = self.app.put("/api/auth/users",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali22", contact="0700-000000", role="admin", password="araali"),)
                                 )                         
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "user does not exist")
        self.assertEqual(response.status_code, 400)   

    def test_user_update_with_missing_keys(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        response = self.app.put("/api/auth/users",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_na="araali22", contact="0700-000000", role="admin", password="araali"),)
                                 )                         
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "a 'key(s)' is missing in update body")
        self.assertEqual(response.status_code, 400)

    def test_user_update_with_white_spaces(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        response = self.app.put("/api/auth/users",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="  araali22", contact="0700-000000", role="admin", password="araali"),)
                                 )                         
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username must have no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_user_update_with_wrong_role(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        response = self.app.put("/api/auth/users",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali22", contact="0700-000000", role="administer", password="araali"),)
                                 )                         
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "role should either be admin or attendant")
        self.assertEqual(response.status_code, 400)

    def test_user_update_with_no_username(self):
        """ Test for successful user register """
        admin_login= self.admin_login()
        response = self.app.post("/api/auth/register",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="araali2", contact="0700-000000", role="attendant", password="araali"),)
                                 )
        response = self.app.put("/api/auth/users",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(user_name="", contact="0700-000000", role="administer", password="araali"),)
                                 )                         
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "usename is missing")
        self.assertEqual(response.status_code, 400)                                             