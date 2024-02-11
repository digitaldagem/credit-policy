import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_post_policy_accept_success():
    payload = dict(
        customer_income = 1000,
        customer_debt = 500,
        payment_remarks_12m = 0,
        payment_remarks = 1,
        customer_age = 20
    )
    response = client.post("/post_policy/", payload)
    data = response.data
    assert response.status_code == 201
    assert data["response"] == "ACCEPT"

@pytest.mark.django_db
def test_post_policy_low_income_success():
    payload = dict(
        customer_income = 499,
        customer_debt = 200,
        payment_remarks_12m = 0,
        payment_remarks = 1,
        customer_age = 20
    )
    response = client.post("/post_policy/", payload)
    data = response.data
    assert response.status_code == 200
    assert data["response"] == "LOW_INCOME"

@pytest.mark.django_db
def test_post_policy_high_debt_success():
    payload = dict(
        customer_income = 1000,
        customer_debt = 501,
        payment_remarks_12m = 0,
        payment_remarks = 1,
        customer_age = 20
    )
    response = client.post("/post_policy/", payload)
    data = response.data
    assert response.status_code == 200
    assert data["response"] == "HIGH_DEBT_FOR_INCOME"

@pytest.mark.django_db
def test_post_policy_remarks_12m_success():
    payload = dict(
        customer_income = 1000,
        customer_debt = 500,
        payment_remarks_12m = 1,
        payment_remarks = 1,
        customer_age = 20
    )
    response = client.post("/post_policy/", payload)
    data = response.data
    assert response.status_code == 200
    assert data["response"] == "PAYMENT_REMARKS_12M"

@pytest.mark.django_db
def test_post_policy_remarks_success():
    payload = dict(
        customer_income = 1000,
        customer_debt = 500,
        payment_remarks_12m = 0,
        payment_remarks = 2,
        customer_age = 20
    )
    response = client.post("/post_policy/", payload)
    data = response.data
    assert response.status_code == 200
    assert data["response"] == "PAYMENT_REMARKS"

@pytest.mark.django_db
def test_post_policy_underage_success():
    payload = dict(
        customer_income = 1000,
        customer_debt = 500,
        payment_remarks_12m = 0,
        payment_remarks = 1,
        customer_age = 13
    )
    response = client.post("/post_policy/", payload)
    data = response.data
    assert response.status_code == 200
    assert data["response"] == "UNDERAGE"

@pytest.mark.django_db
def test_post_policy_require_field_fail():
    payload = dict(
    )
    response = client.post("/post_policy/", payload)
    data = response.data
    assert response.status_code == 400
    assert data["customer_income"] == ["This field is required."]
    assert data["customer_debt"] == ["This field is required."]
    assert data["payment_remarks_12m"] == ["This field is required."]
    assert data["payment_remarks"] == ["This field is required."]
    assert data["customer_age"] == ["This field is required."]

@pytest.mark.django_db
def test_post_policy_require_integer_fail():
    payload = dict(
        customer_income = "one thousand",
        customer_debt = "five hundred",
        payment_remarks_12m = "zero",
        payment_remarks = "one",
        customer_age = "thirteen"
    )
    response = client.post("/post_policy/", payload)
    data = response.data
    assert response.status_code == 400
    assert data["customer_income"] == ["A valid integer is required."]
    assert data["customer_debt"] == ["A valid integer is required."]
    assert data["payment_remarks_12m"] == ["A valid integer is required."]
    assert data["payment_remarks"] == ["A valid integer is required."]
    assert data["customer_age"] == ["A valid integer is required."]