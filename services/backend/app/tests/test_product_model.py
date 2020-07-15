from app.api.products.models import Product


def test_create_product():
    product = Product(3, "testname", 1, 45.89)
    assert product.name == "testname"
    assert product.qty == 1
    assert product.price == 45.89
