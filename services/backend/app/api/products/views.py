from flask import request
from flask_restx import Resource, fields, Namespace, reqparse
from app.api.products.models import Shop, Product

product_namespace = Namespace("product")
shop = Shop()

product = product_namespace.model(
    "Product",
    {
        "sku": fields.Integer(required=True),
        "name": fields.String(required=True),
        "qty": fields.Integer(required=True),
        "price": fields.Fixed(decimals=2, required=True),
    },
)

parser = reqparse.RequestParser()
parser.add_argument("status")


class ProductList(Resource):
    @product_namespace.marshal_with(product, as_list=True)
    @product_namespace.response(200, "returns product list")
    @product_namespace.expect(parser)
    def get(self):
        """returns all, available or unavailable products"""
        args = parser.parse_args()
        status = args["status"]
        if status == "available":
            return shop.available, 200
        if status == "unavailable":
            return shop.unavailable, 200
        return shop.get(), 200

    @product_namespace.expect(product, validate=True)
    @product_namespace.response(201, "<product> was added!")
    @product_namespace.response(400, "Sorry. That product already exists.")
    def post(self):
        """Creates a new product."""
        post_data = request.get_json()
        sku = post_data.get("sku")
        name = post_data.get("name")
        qty = post_data.get("qty")
        price = post_data.get("price")
        response_object = {}

        if len(shop.get(sku)) > 0:
            response_object[
                "message"
            ] = "Sorry. A product with that SKU already exists."
            return response_object, 400
        new_product = Product(sku, name, qty, price)
        shop.add(new_product)
        response_object["message"] = f"Product (SKU{sku}) was added!"
        return response_object, 201

    @product_namespace.expect(product, validate=True)
    @product_namespace.response(201, "<product> was updated!")
    @product_namespace.response(404, "That product does not exist.")
    def put(self):
        """Updates a product."""
        post_data = request.get_json()
        sku = post_data.get("sku")
        name = post_data.get("name")
        qty = post_data.get("qty")
        price = post_data.get("price")
        response_object = {}

        if len(shop.get(sku)) == 0:
            product_namespace.abort(404, f"Product (SKU{sku}) does not exist")
        updated_product = Product(sku, name, qty, price)
        shop.update(updated_product)
        response_object["message"] = f"Product (SKU{sku}) was updated!"
        return response_object, 200

    @product_namespace.response(200, "All products have been deleted!")
    def delete(self):
        """deletes all products from shop"""
        shop.delete()
        response_object = {}
        response_object["message"] = "All products deleted!"
        return response_object, 200


class ProductItem(Resource):
    @product_namespace.marshal_with(product)
    @product_namespace.response(200, "Success")
    @product_namespace.response(404, "Product <SKU> does not exist")
    def get(self, sku):
        """Returns a single product."""
        item = shop.get(sku)
        if not item:
            product_namespace.abort(404, f"Product {sku} does not exist")
        return item[0], 200


product_namespace.add_resource(ProductList, "")
product_namespace.add_resource(ProductItem, "/<int:sku>")
