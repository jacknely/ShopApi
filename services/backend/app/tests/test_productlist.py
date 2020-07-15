import json
import pytest
from app.api.products.views import Shop, Product


def test_add_product(test_app):
    client = test_app.test_client()
    resp = client.post(
        "/product",
        data=json.dumps({"name": "testname", "sku": 2, "qty": 23, "price": 34.66}),
        content_type="application/json",
    )

    assert resp.status_code == 201


def test_add_product_duplicate(test_app):
    client = test_app.test_client()
    client.post(
        "/product",
        data=json.dumps({"name": "testname", "sku": 2, "qty": 23, "price": 34.66}),
        content_type="application/json",
    )
    resp = client.post(
        "/product",
        data=json.dumps({"name": "testname", "sku": 2, "qty": 23, "price": 34.66}),
        content_type="application/json",
    )

    assert resp.status_code == 400


def test_add_product_invalid(test_app):
    client = test_app.test_client()
    resp = client.post(
        "/product", data=json.dumps({}), content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Input payload validation failed" in data["message"]


# def test_add_product_incorrect_price_format(test_app):
#     client = test_app.test_client()
#     resp = client.post(
#         "/product",
#         data=json.dumps({"name": "testname2",
#         "qty": 23,
#         "price": 34}),
#         content_type="application/json",
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert "Input payload validation failed" in data["message"]


def test_get_all_products(test_app):
    client = test_app.test_client()
    client.post(
        "/product",
        data=json.dumps({"name": "testname", "sku": 2, "qty": 23, "price": 34.66}),
        content_type="application/json",
    )
    resp = client.get("/product")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "testname" == data[0]["name"]


def test_get_available_products(test_app):
    client = test_app.test_client()
    client.post(
        "/product",
        data=json.dumps({"name": "testname", "sku": 2, "qty": 23, "price": 34.66}),
        content_type="application/json",
    )
    resp = client.get("/product/?status=available")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "testname" == data[0]["name"]


def test_get_unavailable_products(test_app):
    client = test_app.test_client()
    client.delete("/product")
    client.post(
        "/product",
        data=json.dumps({"name": "testname", "sku": 2, "qty": 0, "price": 34.12}),
        content_type="application/json",
    )
    resp = client.get("/product/?status=unavailable")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "testname" == data[0]["name"]


def test_update_product(test_app):
    client = test_app.test_client()
    client.post(
        "/product",
        data=json.dumps({"name": "testname", "sku": 2, "qty": 23, "price": 34.66}),
        content_type="application/json",
    )
    resp = client.put(
        "/product",
        data=json.dumps({"name": "testname", "sku": 2, "qty": 100, "price": 34.66}),
        content_type="application/json",
    )
    assert resp.status_code == 200
