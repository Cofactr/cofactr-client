"""Part offer class."""
# Standard Modules
from dataclasses import dataclass
from typing import Dict

# Local Modules
from cofactr.schema.flagship.offer import Offer as FlagshipOffer
from cofactr.schema.types import OfferCorrection


@dataclass
class Offer(FlagshipOffer):  # pylint: disable=too-many-instance-attributes
    """Part offer."""

    corrections: Dict[str, OfferCorrection]
