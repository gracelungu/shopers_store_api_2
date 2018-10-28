from app.db.db_manager import DBConnection

class DBFunctions:
    def __init__(self):
        self.connect = DBConnection()
        self.cursor = self.connect.dict_cursor

    def add_new_user(self, user_name, contact, role, password):
        #reegister a user
        query = (
            """INSERT INTO users (username, contact, role, password) VALUES ('{}', '{}', '{}', '{}')""".format(user_name, contact, role, password))
        self.cursor.execute(query)

    def is_username_exist(self,user_name):
        # check if username exists.
        query = ("""SELECT * FROM users where username = '{}'""".format(user_name))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        if user:
            return True
        return False    

    def is_contact_exist(self,contact):
        # check if user contact exists.
        query = ("""SELECT * FROM users where contact = '{}'""".format(contact))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        if user:
            return True
        return False        

    def user_login(self, user_name, password):
        #login a user
        query = ("""SELECT * from users where username = '{}' and password='{}'""".format(user_name, password))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        return user
