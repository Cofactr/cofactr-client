"""Part seller class."""
# Standard Modules
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Seller:  # pylint: disable=too-many-instance-attributes
    """Part seller."""

    label: str
    aliases: List[str]
    authenticity_score: Optional[int]
    availability_score: Optional[int]
    additional_markup: Optional[float]
    additional_fee: Optional[float]
    certifications: List
    #  A separate flag that's independent from accuracy.
    is_buyable: Optional[bool]