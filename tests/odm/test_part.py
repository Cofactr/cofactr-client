"""Test Part class."""
# 3rd Party Modules
import pytest

# Local Modules
from cofactr.graph import GraphAPI
from cofactr.odm.part import Part


from typing import List


def search_parts(query: str, limit=10, external=True) -> List[Part]:
    """Search for parts."""

    graph = GraphAPI()

    cursor = graph.get_products(
        query=query,
        fields="id,statements{spec,image,mfr,mpn,desc,package,numberofpins},offers",
        batch_size=100,
        limit=limit,
        external=external,
        render=False,
    )

    return [Part(**data) for data in cursor]


@pytest.mark.parametrize(
    "mpn",
    ["IRFH4251DTRPBF"],
)
def test_part(mpn: str):
    """Test Part."""

    parts = search_parts(query=mpn, limit=1, external=False)

    assert len(parts) == 1

    part = parts[0]

    assert part.id == "TRGC72NRRA4W"
    assert part.mpn == mpn
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
