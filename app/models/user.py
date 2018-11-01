#model class for a user 

class User(object):
    def __init__(self, user_name, contact, role, password):
        self.user_name = user_name
        self.contact = contact
        self.role = role
        self.password = password
    
    
    

