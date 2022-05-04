"""Test Part class."""
# 3rd Party Modules
from typing import List
import pytest

# Local Modules
from cofactr.odm.core import get_part, get_parts, search_parts


@pytest.mark.parametrize(
    "mpn",
    ["IRFH4251DTRPBF"],
)
def test_search_part(mpn: str):
    """Test Part."""

    parts = search_parts(query=mpn, limit=1, external=False)

    assert len(parts) == 1


@pytest.mark.parametrize(
    "cpid",
    ["TRGC72NRRA4W"],
)
def test_get_part(cpid: str):
    """Test Part."""

    part = get_part(cpid=cpid, external=False)

    assert part

    assert part.id == "TRGC72NRRA4W"
    assert part.mpn == "IRFH4251DTRPBF"
    assert part.hero_image == "https://assets.cofactr.com/TRGC72NRRA4W/part-img.jpg"
    assert (
        part.description
        == "Dual N-Channel 25 V 3.2 mOhm 15 nC HEXFET® Power Mosfet - PQFN 5 x 6 mm"
    )

    spec = part.specs[0]

    assert "property" in spec
    assert "value" in spec

    assert part.terminations == 8

    offer = part.offers[0]

    assert isinstance(offer.authorized, bool)

    # print(offer.seller.name)
    # print(part.availability)


@pytest.mark.parametrize(
    "cpids",
    [["TRGC72NRRA4W", "CCI8TPV75AW2", "CCEEPYIYIALK", "CCV1F7A8UIYH"]],
)
def test_get_parts(cpids: List[str]):
    """Test Part."""

    parts = get_parts(cpids=cpids, external=False)

    assert set(parts) == set(cpids)
