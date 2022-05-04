"""Core functionality."""
# Standard Modules
from typing import List

# Local Modules
from cofactr.graph import GraphAPI
from cofactr.odm.part import Part


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


def get_part(cpid: str, external=True) -> List[Part]:
    """Search for parts."""

    graph = GraphAPI()

    product = graph.get_product(
        id=cpid,
        fields="id,statements{spec,image,mfr,mpn,desc,package,numberofpins},offers",
        external=external,
        render=False,
    )

    return Part(**product["data"]) if product else None


# TODO: Add a bulk fetch function that accepts a list of cpids
# and gets all the data in a single request, returning Part objects.
