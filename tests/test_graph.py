"""Test GraphAPI."""
# Standard Modules
from typing import Any, Dict, List

# 3rd Party Modules
import pytest

# Local Modules
from cofactr.graph import GraphAPI
from cofactr.schema import (
    OfferSchemaName,
    ProductSchemaName,
    SupplierSchemaName,
)


@pytest.mark.parametrize(
    "mpn",
    ["IRFH4251DTRPBF"],
)
def test_search_part(mpn: str):
    """Test searching for parts."""

    graph = GraphAPI()

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
                "hero_image": "https://assets.cofactr.com/TRRQ3ESYFO28/part-img.jpg",
            },
        ),
        (
            "flagship-v2",
            "TRRQ3ESYFO28",
            {
                "id": "TRRQ3ESYFO28",
                "mpn": "IRFH5006TRPBF",
                "hero_image": "https://assets.cofactr.com/TRRQ3ESYFO28/part-img.jpg",
            },
        ),
    ],
)
def test_get_product(schema: ProductSchemaName, cpid: str, expected: Dict[str, Any]):
    """Test getting a product by its ID."""

    graph = GraphAPI()

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
    [["TRGC72NRRA4W", "CCI8TPV75AW2", "CCEEPYIYIALK", "CCV1F7A8UIYH"]],
)
def test_get_products_by_ids(ids: List[str]):
    """Test getting parts in bulk by their IDs."""

    graph = GraphAPI()

    res = graph.get_products_by_ids(
        ids=ids,
        external=False,
        schema=ProductSchemaName.FLAGSHIP,
    )

    assert set(res) == set(ids)


@pytest.mark.parametrize(
    "cpid",
    ["IM60640MOX6H"],
)
def test_get_offers(cpid: str):
    """Test getting offers."""

    graph = GraphAPI()

    flagship_res = graph.get_offers(
        product_id=cpid,
        external=False,
        schema=OfferSchemaName.FLAGSHIP,
    )

    assert flagship_res

    logistics_res = graph.get_offers(
        product_id=cpid,
        external=False,
        schema=OfferSchemaName.LOGISTICS,
    )

    assert logistics_res


@pytest.mark.parametrize("query", ["Digi-Key"])
def test_get_suppliers(query):
    """Test getting suppliers."""

    graph = GraphAPI()

    res = graph.get_suppliers(query=query, schema=SupplierSchemaName.FLAGSHIP)

    data = res["data"]
    assert data

    assert query in {supplier.label for supplier in data}


@pytest.mark.parametrize("org_id", ["622fb450e4c292d8287b0af5"])
def test_get_supplier(org_id):
    """Test getting a supplier."""

    graph = GraphAPI()

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

    graph = GraphAPI()

    res = graph.autocomplete_orgs(query=query, types="supplier")

    completions = res["data"]

    assert completions == expected_completions
