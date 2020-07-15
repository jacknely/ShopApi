import json
import pytest


def test_get_one_product(test_app):
    client = test_app.test_client()
    client.post(
        "/product",
        data=json.dumps({"name": "testname", "sku": 3, "qty": 23, "price": 34.66}),
        content_type="application/json",
    )
    resp = client.get("/product/3")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "testname" == data["name"]


def test_get_one_product_error(test_app):
    client = test_app.test_client()
    client.post(
        "/product",
        data=json.dumps({"name": "testname", "sku": 3, "qty": 23, "price": 34.66}),
        content_type="application/json",
    )
    resp = client.get("/product/2")
    assert resp.status_code == 404
