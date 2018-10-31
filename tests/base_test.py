import unittest
from run import app
from flask import json
from app.db.db_manager import DBConnection
from app.controllers.user_controller import UserController

connection = DBConnection()
user_controller = UserController()

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.user_name = "admin"
        self.contact = "0703-000000"
        self.role = "admin"
        self.password = "admin"
        self.app = app.test_client(self)
        connection.create_tables()
        self.register_admin()
        self.register_attendant()
        
    def tearDown(self):
        # Method to droP tables after the test is run
        connection.delete_tables()

    def register_admin(self):
        user_controller.add_attendant(self.user_name, self.contact, self.role, self.password)
        
    def register_attendant(self):
        user_controller.add_attendant("araali", "0703-000001", "attendant", "araali")
    
    def admin_login(self):
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(user_name=self.user_name, password=self.password))
        )
        reply = json.loads(response.data)
        return reply
    
    def attendant_login(self):
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(user_name="araali", password="araali"))
        )
        reply = json.loads(response.data)
        return reply    