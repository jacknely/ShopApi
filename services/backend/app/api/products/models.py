from flask import current_app


class Shop:
    def __init__(self):
        self.products = []

    def add(self, product):
        """add new product to shop"""
        self.products.append(product)

    def delete(self, sku=""):
        """ delete individual or all products from shop"""
        if sku:
            self.products = [
                product for product in self.products if product.sku is not sku
            ]
        else:
            self.products = []

    def update(self, up_product):
        """update a product in shop"""
        self.products = [
            product for product in self.products if product.sku is not up_product.sku
        ]
        self.products.append(up_product)
        return up_product

    def get(self, sku=""):
        """gets an indivdual product by sku"""
        if sku:
            return [product for product in self.products if product.sku is sku]
        return self.products

    @property
    def available(self):
        """returns a list of available products"""
        return [product for product in self.products if product.qty > 0]

    @property
    def unavailable(self):
        """returns a list of unavailable products"""
        return [product for product in self.products if product.qty == 0]


class Product:
    def __init__(self, sku="", name="", qty="", price=""):
        self.sku = sku
        self.name = name
        self.qty = qty
        self.price = price
