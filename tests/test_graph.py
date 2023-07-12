"""Test GraphAPI."""
# Standard Modules
from datetime import datetime
import json
from pathlib import Path
from typing import Any, Dict, List

# 3rd Party Modules
from dotenv import dotenv_values
import pytest

# Local Modules
from cofactr.graph import GraphAPI, SearchStrategy
from cofactr.schema import (
    OfferSchemaName,
    ProductSchemaName,
    SupplierSchemaName,
)
from cofactr.schema.types import PartialPartInV0

CONFIG = dotenv_values(Path(__file__).parent / "../.env.test")
CLIENT_ID = CONFIG["CLIENT_ID"]
API_KEY = CONFIG["API_KEY"]
TIME_NOW = datetime.utcnow()


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
        schema=ProductSchemaName.FLAGSHIP_V7,
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
            "flagship-v7",
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
    "ids,schema",
    [
        ([], ProductSchemaName.FLAGSHIP_V7),
        (
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
            ],
            ProductSchemaName.FLAGSHIP_V7,
        ),
        (
            [
                "COZSJWDV39RW",
                "IC4ALDY84KAX",
                "IMJ3RXPOZFFK",
                "INKADXLYWJQC",
                "INKADXLYWJQC",
                "TRGC72NRRA4W",
            ],
            ProductSchemaName.FLAGSHIP_CACHE_V4,
        ),
        (
            [
                "XXNGAHF7HD8S",
                "TRCAHGIXODI7",
            ],
            ProductSchemaName.PRICE_SOLVER_V6,
        ),
        (
            [
                "IMC4MDWZJJ09",
            ],
            ProductSchemaName.FLAGSHIP_ALTS_V0,
        ),
    ],
)
def test_get_products_by_ids(ids: List[str], schema: ProductSchemaName):
    """Test getting parts in bulk by their IDs."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    res = graph.get_products_by_ids(
        ids=ids,
        external=False,
        schema=schema,
    )

    assert set(res) == set(ids)


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
        schema=OfferSchemaName.FLAGSHIP_V3,
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

    res = graph.get_suppliers(query=query, schema=SupplierSchemaName.FLAGSHIP_V2)

    data = res["data"]
    assert data

    assert query in {supplier.label for supplier in data}


@pytest.mark.parametrize("org_id", ["622fb450e4c292d8287b0af5"])
def test_get_supplier(org_id):
    """Test getting a supplier."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    res = graph.get_supplier(id=org_id, schema=SupplierSchemaName.FLAGSHIP_V2)

    assert res["data"].id == org_id


@pytest.mark.parametrize(
    "query,expected_completions",
    [
        (
            "digi",
            {
                '{"id": "622fb450e4c292d8287b0be9", "label": "Digi-Key Marketplace"}',
                '{"id": "622fb450e4c292d8287b0af5", "label": "Digi-Key"}',
            },
        )
    ],
)
def test_autocomplete_orgs(query, expected_completions):
    """Test autocompleting orgs."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    res = graph.autocomplete_orgs(query=query, types="supplier")

    completions = res["data"]

    assert {json.dumps(x, sort_keys=True) for x in completions} == expected_completions


@pytest.mark.parametrize(
    "query,expected_completions",
    [
        (
            "Solar Cell",
            {
                '{"id": "solar_cells", "label": "solar cells"}',
            },
        ),
        (
            "sol",
            {
                '{"id": "solid_state_relays", "label": "solid state relays"}',
                '{"id": "solar_cells", "label": "solar cells"}',
                '{"id": "solenoids", "label": "solenoids"}',
            },
        ),
    ],
)
def test_autocomplete_classifications(query, expected_completions):
    """Test autocompleting classifications."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    res = graph.autocomplete_classifications(query=query, types="part_classification")

    completions = res["data"]

    assert {json.dumps(x, sort_keys=True) for x in completions} == expected_completions


@pytest.mark.parametrize("mpns", [["2N7002LT1G", "CC0603JRNPOABN100"]])
def test_get_products_by_searches(mpns):
    """Test executing a batch of product searches."""

    graph = GraphAPI(
        client_id=CLIENT_ID,
        api_key=API_KEY,
        default_product_schema=ProductSchemaName.FLAGSHIP_V7,
    )

    mpn_to_products = graph.get_products_by_searches(
        queries=mpns, search_strategy=SearchStrategy.MPN_SKU_MFR
    )

    assert mpn_to_products["2N7002LT1G"]
    assert mpn_to_products["CC0603JRNPOABN100"]


@pytest.mark.parametrize("ids", [["622fb450e4c292d8287b0b0d"]])
def test_get_suppliers_by_ids(ids):
    """Test getting suppliers in bulk by their IDs."""

    graph = GraphAPI(
        client_id=CLIENT_ID,
        api_key=API_KEY,
        default_supplier_schema=SupplierSchemaName.FLAGSHIP_V2,
    )

    id_to_supplier = graph.get_suppliers_by_ids(ids=ids)

    assert set(id_to_supplier.keys()) == set(ids)


@pytest.mark.parametrize(
    "ids,expected_id_to_canonical_id",
    [
        ([], {}),
        (["abc"], {"abc": None}),
        (
            [
                "COZSJWDV39RW",
                "IC4ALDY84KAX",
                "IMJ3RXPOZFFK",
                "INKADXLYWJQC",
                "TRGC72NRRA4W",
            ],
            {
                "COZSJWDV39RW": "COZSJWDV39RW",
                "IC4ALDY84KAX": "IC4ALDY84KAX",
                "IMJ3RXPOZFFK": "IM8U4NOIMGD0",
                "INKADXLYWJQC": "INH7OHMZ0R0W",
                "TRGC72NRRA4W": "TRK8NOFDCUFI",
            },
        ),
    ],
)
def test_get_canonical_product_ids(ids, expected_id_to_canonical_id):
    """Test getting canonical product IDs."""

    graph = GraphAPI(
        client_id=CLIENT_ID,
        api_key=API_KEY,
        default_supplier_schema=SupplierSchemaName.FLAGSHIP_V2,
    )

    actual_id_to_canonical_id = graph.get_canonical_product_ids(ids=ids)

    assert actual_id_to_canonical_id == expected_id_to_canonical_id


@pytest.mark.parametrize(
    "product_id,data,owner_id",
    [
        ("COZSJWDV39RW", PartialPartInV0(description="test value"), "sdk test"),
        ("COZSJWDV39RW", PartialPartInV0(description=None), "sdk test"),
        (
            "COZSJWDV39RW",
            PartialPartInV0(custom_id="test value", lifecycle_status="Production"),
            "sdk test",
        ),
    ],
)
def test_update_product(product_id, data, owner_id):
    """Test updating a product."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    graph.update_product(product_id=product_id, data=data, owner_id=owner_id)


@pytest.mark.parametrize(
    "id_to_custom_id,owner_id",
    [
        (
            {
                "XXL0Z0HB5JGI": f"example custom ID: {TIME_NOW}",
                "IMC4MDWZJJ09": f"another example custom ID: {TIME_NOW}",
            },
            "sdk test",
        ),
    ],
)
def test_set_custom_product_ids(id_to_custom_id, owner_id):
    """Test setting custom product IDs."""

    graph = GraphAPI(
        client_id=CLIENT_ID,
        api_key=API_KEY,
        default_supplier_schema=SupplierSchemaName.FLAGSHIP_V2,
    )

    graph.set_custom_product_ids(id_to_custom_id=id_to_custom_id, owner_id=owner_id)
