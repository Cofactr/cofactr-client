"""Cofactr client."""
# Python Modules
import json
from typing import List, Literal, Optional

# 3rd Party Modules
import urllib3

Protocol = Literal["http", "https"]


class GraphAPI:
    """A client-side representation of the Cofactr graph API."""

    PROTOCOL: Protocol = "https"
    HOST = "graph.cofactr.com"

    def __init__(
        self, protocol: Optional[Protocol] = PROTOCOL, host: Optional[str] = HOST
    ):

        self.url = f"{protocol}://{host}"
        self.http = urllib3.PoolManager()

    def check_health(self):
        """Check the operational status of the service."""

        res = self.http.request("GET", f"{self.url}/health")

        return json.loads(res.data.decode("utf-8"))

    def get_products(
        self,
        query: Optional[str] = None,
        fields: Optional[List[str]] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        external: Optional[bool] = None,
    ):
        """Get products.

        Args:
            query: Search query.
            fields: Used to filter properties that the response should contain. A field can be a
                concrete property like "mpn" or an abstract group of properties like "assembly".
            before: Upper page boundry, expressed as a product ID.
            after: Lower page boundry, expressed as a product ID.
            limit: Maximum number of entities the response should contain.
            external: Whether to query external sources.
        """

        res = self.http.request(
            "GET",
            f"{self.url}/products",
            fields={
                query: query,
                fields: fields,
                before: before,
                after: after,
                limit: limit,
                external: external,
            },
        )

        return json.loads(res.data.decode("utf-8"))

    def get_orgs(
        self,
        query: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        limit: Optional[int] = None,
    ):
        """Get organizations.

        Args:
            query: Search query.
            before: Upper page boundry, expressed as a product ID.
            after: Lower page boundry, expressed as a product ID.
            limit: Maximum number of entities the response should contain.
        """

        res = self.http.request(
            "GET",
            f"{self.url}/orgs",
            fields={
                query: query,
                before: before,
                after: after,
                limit: limit,
            },
        )

        return json.loads(res.data.decode("utf-8"))

    def get_product(self, id: str):
        """Get product."""

        res = self.http.request("GET", f"{self.url}/products/{id}")

        return json.loads(res.data.decode("utf-8"))

    def get_org(self, id: str):
        """Get organization."""

        res = self.http.request("GET", f"{self.url}/orgs/{id}")

        return json.loads(res.data.decode("utf-8"))
