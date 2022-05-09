"""Test Part class."""
# 3rd Party Modules
from typing import List
import pytest

# Local Modules
from cofactr.core import get_part, get_parts, search_parts


@pytest.mark.parametrize(
    "mpn",
    ["IRFH4251DTRPBF"],
)
def test_search_part(mpn: str):
    """Test Part."""

    res = search_parts(query=mpn, limit=1, external=False)

    assert len(res["data"]) > 0


@pytest.mark.parametrize(
    "cpid",
    ["TRGC72NRRA4W"],
)
def test_get_part(cpid: str):
    """Test Part."""

    res = get_part(id=cpid, external=False)

    part = res["data"]

    assert part
    assert part.id == "TRGC72NRRA4W"
    assert part.mpn == "IRFH4251DTRPBF"
    assert part.hero_image == "https://assets.cofactr.com/TRGC72NRRA4W/part-img.jpg"
    assert (
        part.description
        == "Dual N-Channel 25 V 3.2 mOhm 15 nC HEXFET® Power Mosfet - PQFN 5 x 6 mm"
    )

    assert {"width", "packaging"}.issubset(set(part.specs))


@pytest.mark.parametrize(
    "ids",
    [["TRGC72NRRA4W", "CCI8TPV75AW2", "CCEEPYIYIALK", "CCV1F7A8UIYH"]],
)
def test_get_parts(ids: List[str]):
    """Test Part."""

    responses = get_parts(ids=ids, external=False)

    assert set(responses) == set(ids)
