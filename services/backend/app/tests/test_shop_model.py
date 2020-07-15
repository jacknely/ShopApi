from app.api.products.models import Shop, Product


def test_add_product():
    product = Product(3, "testname", 1, 45.89)
    shop = Shop()
    shop.add(product)
    assert len(shop.products) == 1


def test_delete_product():
    product = Product(3, "testname", 1, 45.89)
    shop = Shop()
    shop.add(product)
    assert len(shop.products) == 1
    shop.delete(3)
    assert len(shop.products) == 0


def test_delete_all():
    product = Product(3, "testname", 1, 45.89)
    shop = Shop()
    shop.add(product)
    assert len(shop.products) == 1
    shop.delete()
    assert len(shop.products) == 0


def test_update():
    product = Product(3, "testname", 1, 45.89)
    shop = Shop()
    shop.add(product)
    assert len(shop.products) == 1
    updated_product = Product(3, "testname", 100, 45.89)
    shop.update(updated_product)
    assert shop.products[0].qty == 100
    assert len(shop.products) == 1


def test_get_product_exists():
    product = Product(3, "testname", 1, 45.89)
    shop = Shop()
    shop.add(product)
    assert len(shop.products) == 1
    shop.get(3)
    assert len(shop.products) == 1


def test_get_product_not_exists():
    shop = Shop()
    assert len(shop.products) == 0
    shop.get(3)
    assert len(shop.products) == 0


def test_get_available_products():
    product = Product(3, "testname", 1, 45.89)
    shop = Shop()
    shop.add(product)
    assert len(shop.products) == 1
    assert len(shop.available) == 1


def test_get_unavailable_products():
    product = Product(3, "testname", 0, 45.89)
    shop = Shop()
    shop.add(product)
    assert len(shop.products) == 1
    assert len(shop.unavailable) == 1
