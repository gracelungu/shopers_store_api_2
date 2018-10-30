from flask import jsonify, request, Blueprint
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.validation import Validation
from app.auth.authentication import admin_permission_required
from app.controllers.product_controller import ProductController

validate = Validation()
product_controller = ProductController()
views_blueprint = Blueprint("views_blueprint", __name__)


class AddProduct(MethodView):
    # @jwt_required
    @admin_permission_required
    def post(self):
        try:
            data = request.get_json()
            search_keys = ("product", "quantity", "unit_price")
            if all(key in data.keys() for key in search_keys):
                product = data.get("product")
                quantity = data.get("quantity")
                unit_price = data.get("unit_price")

                invalid = validate.product_validation(
                    product, quantity, unit_price)
                if invalid:
                    return jsonify({"message": invalid}), 400
                product_exists = product_controller.does_product_exist(
                    product_name=product)
                if product_exists:
                    new_quantity = product_exists["quantity"] + int(quantity)
                    product_controller.update_product(product_name=product,
                                                      quantity=new_quantity, unit_price=unit_price, product_id=product_exists["product_id"])
                    return jsonify({
                        "message":
                            "product already exits, so its quantity has been updated", "Updated Product":
                            product_controller.get_single_product(product_exists["product_id"])}), 200
                product_added = product_controller.add_product(product_name=product, quantity=int(
                    quantity), unit_price=int(unit_price))
                if product_added:
                    return jsonify({
                        "message":
                        "product successfully added.", "New Product": product_controller.does_product_exist(product_name=product)
                    }), 201
                return jsonify({"message": "product not added"}), 400
            return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400
        except Exception as exception:
            return jsonify({"message": str(exception)}), 400

class DeleteProduct(MethodView):
    def delete(self, product_id):
        invalid = validate.validate_input_type(product_id)
        if invalid:
            return jsonify({"message": invalid}), 400
        delete = product_controller.delete_product(product_id=product_id)
        if delete:
            return jsonify({"message": "product successfully deleted"}), 200
        else:
            return jsonify({"message": "product not deleted, or doesn't exist"}), 400

add_product_view = AddProduct.as_view("add_product_view")
delete_product_view = DeleteProduct.as_view("delete_product_view")

views_blueprint.add_url_rule("/api/v1/products", view_func=add_product_view, methods=["POST"])
views_blueprint.add_url_rule("/api/v1/products/<product_id>", view_func=delete_product_view, methods=["DELETE"])

