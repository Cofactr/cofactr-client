"""Test Part class."""
# 3rd Party Modules
import pytest

# Local Modules
from cofactr.odm.core import get_part, search_parts


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

    print(offer.seller.name)

    print(part.availability)
