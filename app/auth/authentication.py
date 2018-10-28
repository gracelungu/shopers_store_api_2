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
