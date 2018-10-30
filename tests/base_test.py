import unittest
from run import app
from app.db.db_manager import DBConnection

connection = DBConnection()

class BaseTestCase(unittest.TestCase):

    def create_app(self):
        pass
        # """
        # Create an instance of the app with the testing configuration
        # """
        # app.config.from_object(app_config["testing"])
        # return app

    def setUp(self):
        pass
        # self.app = app.test_client(self)
        # connection.create_test_tables()
        
    def tearDown(self):
        pass
        """
        Method to droP tables after the test is run
        """
        # connection.delete_test_tables()