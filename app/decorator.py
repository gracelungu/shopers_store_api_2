from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from app.controllers.user_controller import UserController
user_controller = UserController()

def admin_permission_required(yx):
    #  A decorator function to wrap and replace the normal jwt_required function
    @wraps(yx)
    def decorated_function(*args, **kwargs):
        # check role of user in token.
        verify_jwt_in_request()
        logged_user = get_jwt_identity()
        user_role = user_controller.get_user_role(user_name=logged_user)
        if user_role["role"] != 'admin':
            return jsonify({"message": "You need Admin previllages to access this route"}), 403
        else:
            return yx(*args, **kwargs)
    return decorated_function