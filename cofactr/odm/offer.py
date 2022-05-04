# Standard Modules
from typing import Optional
from cofactr.helpers import find_preferred, get_path

# Local Modules
from cofactr.odm.seller import Seller


class Offer:
    def __init__(self, part, offer, seller):
        self._part = part
        self._offer = offer

        self._authorized = get_path(
            find_preferred(
                get_path(seller, ["statements", "is_authorized_seller"]), default={}
            ),
            ["mainsnak", "datavalue", "value"],
        )
        self._seller = Seller(**seller)

    @property
    def authorized(self) -> bool:
        return self._authorized

    @property
    def seller(self) -> Seller:
        return self._seller

    @property
    def stock(self) -> int:
        return self._offer["inventory_level"]

    @property
    def lead(self) -> int:
        return self._offer["factory_lead_days"]

    @property
    def moq(self) -> int:
        """Minimum order quantity."""
        return self._offer["moq"]

    @property
    def multiple(self) -> int:
        return self._offer["order_multiple"]

    @property
    def foreign(self) -> Optional[bool]:
        return None  # was this price originally in a different currency than USD

    @property
    def ship_from_country(self) -> Optional[str]:
        return None  # 2 letter country code for current location of this part

    @property
    def prices(self):
        return self._offer["prices"]

    @property
    def reported_on(self):
        """Time that we received/cached this offer data."""
        return self._offer["updated_at"]["$date"]

    # def calculate_tariffs(quant, destination_country) -> float:
    #     return  # estimated tar

    # def is_exportable(destination_country) -> bool:
    #     return
