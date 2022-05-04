"""Part class."""
# Standard Modules
from typing import List, Optional
from cofactr.helpers import find_preferred

# Local Modules
from cofactr.kb.entity.types import OfferGroup, Statements
from cofactr.odm.offer import Offer
from cofactr.render import mainsnak_to_str
from cofactr.helpers import identity

TYPE_TO_VALUE_ACCESSOR = {
    "boolean": lambda v: {
        "value": v["value"],
    },
    "external_id": lambda v: {
        "value": v["value"],
    },
    "monolingual_text": lambda v: {
        "value": v["value"]["text"],
    },
    "quantity": lambda v: {
        "value": v["amount"],
        "unit": v["unit"],
    },
    "url": lambda v: {
        "value": v["value"],
    },
    "time": lambda v: {
        "value": v["value"],
    },
}


def spec_value(mainsnak):
    """Flatten and select only critical fields."""
    datatype = mainsnak["datatype"]
    value_accessor = TYPE_TO_VALUE_ACCESSOR.get(
        datatype,
        identity,
    )
    datavalue = mainsnak["datavalue"]

    return value_accessor(datavalue)


class Part:
    """Part."""

    def __init__(
        self,
        id: str,
        statements: Statements,
        offers: List[OfferGroup],
    ) -> None:
        self.id = id
        self._statements = statements
        self._offers = offers

    @property
    def description(self) -> str:
        """Description."""
        return mainsnak_to_str(find_preferred(self._statements["desc"]))

    @property
    def specs(self):
        """Specification data."""

        preferred_objs = {
            prop: find_preferred(objs)
            for prop, objs in (self._statements["spec"] or {}).items()
        }

        return [
            {"property": prop, **spec_value(obj["mainsnak"])}
            for prop, obj in preferred_objs.items()
        ]

    @property
    def hero_image(self) -> str:
        """Hero image URL."""
        return mainsnak_to_str(find_preferred(self._statements["image"]))

    @property
    def mpn(self) -> str:
        """Canonical manufacturer part number."""
        return mainsnak_to_str(find_preferred(self._statements["mpn"]))

    @property
    def mfr(self) -> str:
        """Manufacturer name."""
        return mainsnak_to_str(find_preferred(self._statements["mfr"]))

    @property
    def documents(self):
        # TODO: Add prop group.
        return []

    @property
    def msl(self) -> int:
        """Moisture sensitivity level."""
        # TODO: Will come from Digi-Key.
        return 1

    @property
    def package(self) -> Optional[str]:
        return mainsnak_to_str(find_preferred(self._statements["package"]))

    @property
    def terminations(self) -> Optional[int]:
        value = mainsnak_to_str(find_preferred(self._statements["numberofpins"]))

        try:
            return int(value)
        except ValueError:
            return None

    @property
    def data_age(self):
        """timestamp of oldest piece of offer data"""
        return None

    @property
    def offers(self):
        offers_ = []

        for offer_group in self._offers or []:
            seller = offer_group["seller"]

            for offer in offer_group["offers"]:
                offers_.append(Offer(part=self, offer=offer, seller=seller))

        return offers_

    @property
    def availability(self):
        buyable = 0
        quotable = 0
        maybe = 0

        offers_ = self.offers
        # TODO: Find meaning of each.

        return {"buyable": 0, "quotable": 0, "maybe": 0}

    #     def calc_overage(quant: int) -> int:
    #         return quant
