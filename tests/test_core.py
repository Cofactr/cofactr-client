"""Test Part class."""
# Standard Modules
from typing import Any, Dict, List

# 3rd Party Modules
import pytest

# Local Modules
from cofactr.graph import GraphAPI
from cofactr.schema import ProductSchemaName


@pytest.mark.parametrize(
    "mpn",
    ["IRFH4251DTRPBF"],
)
def test_search_part(mpn: str):
    """Test Part."""

    graph = GraphAPI()

    res = graph.get_products(
        query=mpn,
        limit=1,
        external=False,
        schema=ProductSchemaName.FLAGSHIP,
    )

    assert len(res["data"]) > 0


@pytest.mark.parametrize(
    "cpid,expected",
    [
        (
            "TRGC72NRRA4W",
            {
                "id": "TRGC72NRRA4W",
                "mpn": "IRFH4251DTRPBF",
                "hero_image": "https://assets.cofactr.com/TRGC72NRRA4W/part-img.jpg",
            },
        ),
        (
            "TR8LQK8DAC2G",
            {
                "id": "TR8LQK8DAC2G",
                "mpn": "2N7002",
                "hero_image": "https://assets.cofactr.com/TR8LQK8DAC2G/part-img.jpg",
            },
        ),
    ],
)
def test_get_part(cpid: str, expected: Dict[str, Any]):
    """Test Part."""

    graph = GraphAPI()

    res = graph.get_product(
        id=cpid,
        external=False,
        schema=ProductSchemaName.FLAGSHIP,
    )

    part = res["data"]
    assert part

    for attr, expected_value in expected.items():
        assert getattr(part, attr) == expected_value

    assert {"width", "packaging"}.issubset(set(part.specs))


@pytest.mark.parametrize(
    "ids",
    [["TRGC72NRRA4W", "CCI8TPV75AW2", "CCEEPYIYIALK", "CCV1F7A8UIYH"]],
)
def test_get_parts(ids: List[str]):
    """Test Part."""

    graph = GraphAPI()

    res = graph.get_parts_by_ids(
        ids=ids,
        external=False,
        schema=ProductSchemaName.FLAGSHIP,
    )

    assert set(res) == set(ids)
