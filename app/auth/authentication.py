from flask import request, jsonify, Blueprint
from flask.views import MethodView
from functools import wraps
from flask_jwt_extended import create_access_token, get_jwt_identity, verify_jwt_in_request
from app.validation import Validation
from app.controllers.user_controller import UserController
import datetime

validate = Validation()
user_controller = UserController()
auth_blueprint = Blueprint("auth_blueprint", __name__)

class RegisterAttendant(MethodView):
    @admin_permission_required
    def post(self):
        data = request.get_json()
        search_keys = ("user_name","contact","role","password")
        if all(key in data.keys() for key in search_keys):
            user_name = data.get("user_name")
            contact = data.get("contact")
            role = data.get("role")
            password = data.get("password")

            invalid = validate.validate_user(user_name, contact, role, password)
            if invalid:
                return jsonify({"message": invalid}), 400
            username_exists = user_controller.check_if_user_exists(user_name=user_name)
            if username_exists:
                return jsonify({"message": "username exists"}), 409
            contact_exists = user_controller.check_if_contact_exists(contact=contact)
            if contact_exists:
                return jsonify({"message": "contact exists"}), 409
            new_user = user_controller.add_attendant(user_name=user_name,contact=contact,role=role, password=password)
            if new_user:
                return jsonify({"message": "Attendant account created"}), 201
            else:
                return jsonify({"message": "Account not created"}), 400
        return jsonify({"message": "a 'key(s)' is missing in your registration body"}), 400

registration_view = RegisterAttendant.as_view("registration_view")
auth_blueprint.add_url_rule("/api/auth/register",view_func=registration_view, methods=["POST"])

class Login(MethodView):
    def post(self):
        data = request.get_json()
        search_keys = ("user_name", "password")
        if all(key in data.keys() for key in search_keys):
            user_name = data.get("user_name")
            password = data.get("password")

            invalid = validate.login_validation(user_name, password)
            if invalid:
                return jsonify({"message": invalid}), 400

            user_token = {}
            expires = datetime.timedelta(days=1)
            grant_access = user_controller.user_login(user_name=user_name, password=password)
            if grant_access:
                access_token = create_access_token(identity= grant_access["username"], expires_delta=expires)
                user_token["logged in user"]=user_name
                user_token["token"] = access_token
                return jsonify(user_token), 200
            return jsonify({"message": "user does not exist"}), 404
        return jsonify({"message": "a 'key(s)' is missing in login body"}), 400

login_view = Login.as_view("login_view")
auth_blueprint.add_url_rule("/api/auth/login",view_func=login_view, methods=["POST"])

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
