"""Core functionality."""
# Standard Modules
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List

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


def get_part(id: str, external=True) -> List[Part]:
    """Get a part."""

    graph = GraphAPI()

    product = graph.get_product(
        id=id,
        fields="id,statements{spec,image,mfr,mpn,desc,package,numberofpins},offers",
        external=external,
        render=False,
    )

    return Part(**product["data"]) if product else None


def get_parts(ids: List[str], external=True) -> Dict[str, Part]:
    """Get a batch of parts.

    Note:
        Will evolve to use a batched requests. Where, for example, each request
        contains 50 part IDs.
    """
    with ThreadPoolExecutor() as executor:
        return dict(
            zip(
                ids,
                executor.map(lambda cpid: get_part(cpid, external=external), ids),
            )
        )
