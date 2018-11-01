from flask import jsonify, request, Blueprint
from flask.views import MethodView
from datetime import datetime
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.validation import Validation
from app.decorator import admin_permission_required
from app.controllers.product_controller import ProductController
from app.controllers.sale_controller import SaleController
from app.controllers.user_controller import UserController
from app.db.db_functions import DBFunctions

validate = Validation()
product_controller = ProductController()
user_controller = UserController()
sale_controller = SaleController()
db_func = DBFunctions()
views_blueprint = Blueprint("views_blueprint", __name__)

"""PRODUCT VIEWS"""
class AddProduct(MethodView):
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
                            "product already exits, so its quantity has been updated", "product":
                            product_controller.get_single_product(product_exists["product_id"])}), 200
                product_added = product_controller.add_product(product_name=product, quantity=int(
                    quantity), unit_price=int(unit_price))
                if product_added:
                    return jsonify({
                        "message":
                        "product successfully added.", "product": product_controller.does_product_exist(product_name=product)
                    }), 201
                return jsonify({"message": "product not added"}), 400
            return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400
        except Exception as exception:
            return jsonify({"message": str(exception)}), 400


class FetchAllProducts(MethodView):
    @jwt_required
    def get(self):
        all_products = product_controller.fetch_all_products()
        if all_products:
            return jsonify({"available_products": all_products}), 200
        return jsonify({"message": "no products added yet"}), 404


class FetchSingleProduct(MethodView):
    @jwt_required
    def get(self, product_id):
        invalid = validate.validate_input_type(product_id)
        if invalid:
            return jsonify({"message": invalid}), 400
        product_details = product_controller.get_single_product(
            product_id=product_id)
        if product_details:
            return jsonify({"product_details": product_details}), 200
        return jsonify({"message": "product not added yet"}), 404


class DeleteProduct(MethodView):
    @admin_permission_required
    def delete(self, product_id):
        invalid = validate.validate_input_type(product_id)
        if invalid:
            return jsonify({"message": invalid}), 400
        delete = product_controller.delete_product(product_id=product_id)
        if delete:
            return jsonify({"message": "product successfully deleted"}), 200
        else:
            return jsonify({"message": "product not deleted, or doesn't exist"}), 400


class UpdateProduct(MethodView):
    @admin_permission_required
    def put(self, product_id):
        invalid_id = validate.validate_input_type(product_id)
        if invalid_id:
            return jsonify({"message": invalid_id}), 400
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
            update = product_controller.update_product(
                product_name=product, quantity=quantity, unit_price=unit_price, product_id=product_id)
            if update:
                return jsonify({
                    "message":
                        "product successfully updated.", "product": product_controller.get_single_product(product_id=product_id)
                }), 200
            return jsonify({"message": "product not updated or doesn't exist"}), 400
        return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400


add_product_view = AddProduct.as_view("add_product_view")
fetch_all_products_view = FetchAllProducts.as_view("fetch_all_products_view")
fetch_single_product_view = FetchSingleProduct.as_view(
    "fetch_single_product_view")
delete_product_view = DeleteProduct.as_view("delete_product_view")
update_product_view = UpdateProduct.as_view("update_product_view")

views_blueprint.add_url_rule(
    "/api/v2/products", view_func=add_product_view, methods=["POST"])
views_blueprint.add_url_rule(
    "/api/v2/products", view_func=fetch_all_products_view, methods=["GET"])
views_blueprint.add_url_rule("/api/v2/products/<product_id>",
                             view_func=fetch_single_product_view, methods=["GET"])
views_blueprint.add_url_rule(
    "/api/v2/products/<product_id>", view_func=delete_product_view, methods=["DELETE"])
views_blueprint.add_url_rule(
    "/api/v2/products/<product_id>", view_func=update_product_view, methods=["PUT"])

"""SALES VIEWS"""
class CreateSalesRecord(MethodView):
    @jwt_required
    def post(self):
        data = request.get_json()
        search_keys = ("product_id", "quantity")
        if all(key in data.keys() for key in search_keys):
            product_id = data.get("product_id")
            quantity = data.get("quantity")
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            attendant = get_jwt_identity()
            invalid_quantity = validate.validate_input_type(quantity)
            if invalid_quantity:
                return jsonify({"message": invalid_quantity}), 400
            invalid_id = validate.validate_input_type(product_id)
            if invalid_id:
                return jsonify({"message": invalid_id}), 400
            make_sale = sale_controller.add_sale_record(
                product_id=product_id, quantity=quantity, attendant=attendant, date=date)
            if make_sale:
                return jsonify({"message": "sale record successfully added", "sale": db_func.get_newest_sale()}), 201
            else:
                return jsonify({"message": "sale record not added. Product not available or is at minimum quantity"}), 400

class FetchAllSales(MethodView):
    @jwt_required
    def get(self):
        logged_user = get_jwt_identity()
        user_role = user_controller.get_user_role(user_name=logged_user)
        if user_role["role"] == 'admin':
            all_sales = sale_controller.fetch_all_sales()
        elif user_role["role"] == 'attendant':
            all_sales = sale_controller.fetch_all_sales_for_user(user_name=logged_user)
        if all_sales:
            return jsonify({"sale_records": all_sales}), 200
        return jsonify({"message": "no sles recorded yet"}), 404    

class FetchSingleSaleRecord(MethodView):
    @jwt_required
    def get(self, sale_id):
        invalid = validate.validate_input_type(sale_id)
        if invalid:
            return jsonify({"message": invalid}), 400
        logged_user = get_jwt_identity()
        user_role = user_controller.get_user_role(user_name=logged_user)
        if user_role["role"] == 'admin':    
            sale_record = sale_controller.fetch_single_sale(sale_id=sale_id)
        elif user_role["role"] == 'attendant':
            sale_record = sale_controller.fetch_single_sale_for_user(sale_id=sale_id, user_name=logged_user)
        if sale_record:
            return jsonify({"sale_details": sale_record}), 200
        return jsonify({"message": "sale record not added yet"}), 404


make_sales_view = CreateSalesRecord.as_view("make_sales_view")
all_sales_view = FetchAllSales.as_view("all_sales_view")
single_sales_view = FetchSingleSaleRecord.as_view("single_sales_view")


views_blueprint.add_url_rule("/api/v2/sales", view_func=make_sales_view, methods=["POST"])
views_blueprint.add_url_rule("/api/v2/sales", view_func=all_sales_view, methods=["GET"])
views_blueprint.add_url_rule("/api/v2/sales/<sale_id>", view_func=single_sales_view, methods=["GET"])


