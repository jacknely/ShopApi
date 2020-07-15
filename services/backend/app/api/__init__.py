from flask_restx import Api

from app.api.ping import ping_namespace
from app.api.products.views import product_namespace

api = Api(version="1.0", title="Product API", doc="/doc/")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(product_namespace, path="/product")
