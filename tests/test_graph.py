"""Test GraphAPI."""
# Standard Modules
from pathlib import Path
from typing import Any, Dict, List

# 3rd Party Modules
from dotenv import dotenv_values
import pytest

# Local Modules
from cofactr.graph import GraphAPI
from cofactr.schema import (
    OfferSchemaName,
    ProductSchemaName,
    SupplierSchemaName,
)

CONFIG = dotenv_values(Path(__file__).parent / "../.env.test")
CLIENT_ID = CONFIG["CLIENT_ID"]
API_KEY = CONFIG["API_KEY"]

@pytest.mark.parametrize(
    "mpn",
    ["IRFH4251DTRPBF"],
)
def test_search_part(mpn: str):
    """Test searching for parts."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    res = graph.get_products(
        query=mpn,
        limit=1,
        external=False,
        schema=ProductSchemaName.FLAGSHIP,
    )

    assert len(res["data"]) > 0


@pytest.mark.parametrize(
    "schema,cpid,expected",
    [
        (
            "flagship",
            "TRRQ3ESYFO28",
            {
                "id": "TRRQ3ESYFO28",
                "mpn": "IRFH5006TRPBF",
                # "hero_image": "https://assets.cofactr.com/TRRQ3ESYFO28/part-img.jpg",
            },
        ),
        (
            "flagship-v2",
            "TRRQ3ESYFO28",
            {
                "id": "TRRQ3ESYFO28",
                "mpn": "IRFH5006TRPBF",
                # "hero_image": "https://assets.cofactr.com/TRRQ3ESYFO28/part-img.jpg",
            },
        ),
    ],
)
def test_get_product(schema: ProductSchemaName, cpid: str, expected: Dict[str, Any]):
    """Test getting a product by its ID."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    res = graph.get_product(
        id=cpid,
        external=False,
        schema=ProductSchemaName(schema),
    )

    part = res["data"]
    assert part

    for attr, expected_value in expected.items():
        assert getattr(part, attr) == expected_value

    assert {"width", "packaging"}.issubset({s["id"] for s in part.specs})


@pytest.mark.parametrize(
    "ids",
    [
        [
            "CCI8TPV75AW2",
            "CCEEPYIYIALK",
            "CCV1F7A8UIYH",
            "INY4PO7KBQNY",
            "CCCQSA3G9SMR",
            "CCVSTE6K2AFU",
            "RCA8AQY5TJSW",
            "RC2VSL85Q661",
            "RCQSO03FR280",
            "RCXSQXQNTH42",
            "RCOORAYN6TYZ",
            "CCGJZ8YO23N9",
            "CCWA81Z4WGKH",
            "CCLTDD7R51AD",
            "CCH6S1HI9CHZ",
            "CCCFI2O45S02",
            "COPT8HZW65QI",
            "COY1W16Z1VWA",
            "RCU9WS1H4LSD",
            "RCJYRQIWJNWH",
            "XX8HGWW7521L",
        ]
    ],
)
def test_get_products_by_ids(ids: List[str]):
    """Test getting parts in bulk by their IDs."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    res = graph.get_products_by_ids(
        ids=ids,
        external=False,
        schema=ProductSchemaName.FLAGSHIP_V3,
    )

    assert set(res) == set(ids)

    res = graph.get_products_by_ids(
        ids=[],
        external=False,
        schema=ProductSchemaName.FLAGSHIP_V3,
    )


@pytest.mark.parametrize(
    "cpid",
    ["CCV1F7A8UIYH"],
)
def test_get_offers(cpid: str):
    """Test getting offers."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    flagship_res = graph.get_offers(
        product_id=cpid,
        external=False,
        schema=OfferSchemaName.FLAGSHIP,
    )

    assert flagship_res

    logistics_res = graph.get_offers(
        product_id=cpid,
        external=False,
        schema=OfferSchemaName.LOGISTICS_V2,
    )

    assert logistics_res


@pytest.mark.parametrize("query", ["Digi-Key"])
def test_get_suppliers(query):
    """Test getting suppliers."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    res = graph.get_suppliers(query=query, schema=SupplierSchemaName.FLAGSHIP)

    data = res["data"]
    assert data

    assert query in {supplier.label for supplier in data}


@pytest.mark.parametrize("org_id", ["622fb450e4c292d8287b0af5"])
def test_get_supplier(org_id):
    """Test getting a supplier."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    res = graph.get_supplier(id=org_id, schema=SupplierSchemaName.FLAGSHIP)

    assert res["data"].id == org_id


@pytest.mark.parametrize(
    "query,expected_completions",
    [
        (
            "digi",
            [
                {"id": "622fb450e4c292d8287b0af5", "label": "Digi-Key"},
                {"id": "622fb450e4c292d8287b0be9", "label": "Digi-Key Marketplace"},
            ],
        )
    ],
)
def test_autocomplete_orgs(query, expected_completions):
    """Test autocompleting orgs."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    res = graph.autocomplete_orgs(query=query, types="supplier")

    completions = res["data"]

    assert completions == expected_completions


@pytest.mark.parametrize("mpns", [["2N7002LT1G", "CC0603JRNPOABN100"]])
def test_get_products_by_searches(mpns):
    """Test executing a batch of product searches."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY, default_product_schema=ProductSchemaName.FLAGSHIP_V3)

    mpn_to_products = graph.get_products_by_searches(queries=mpns)

    assert mpn_to_products["2N7002LT1G"]
    assert mpn_to_products["CC0603JRNPOABN100"]


@pytest.mark.parametrize("ids", [["622fb450e4c292d8287b0af5", "622fb450e4c292d8287b0b00"]])
def test_get_suppliers_by_ids(ids):
    """Test getting suppliers in bulk by their IDs."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY, default_supplier_schema=SupplierSchemaName.FLAGSHIP)

    id_to_supplier = graph.get_suppliers_by_ids(ids=ids)

    assert set(id_to_supplier.keys()) == set(ids)
