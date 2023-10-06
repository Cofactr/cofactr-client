"""Part seller class."""
# Standard Modules
from dataclasses import dataclass

# Local Modules
from cofactr.schema.flagship_v6.seller import Seller as FlagshipV6Seller


@dataclass
class Seller(FlagshipV6Seller):
    """Part seller."""
