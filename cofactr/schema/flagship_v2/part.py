"""Part class."""
# Standard Modules
from dataclasses import dataclass
from typing import List, Literal

# Local Modules
from cofactr.kb.entity.types import PricePoint
from cofactr.schema.flagship.part import Part as FlagshipPart

TerminationType = Literal[
    "other",
    "SMT",
    "THT",
    "pressed fit",
    "hybrid of SMT and THT",
    "hybrid of pressed fit and SMT",
    "hybrid of pressed fit and THT",
]


@dataclass
class Part(FlagshipPart):
    """Part."""

    buyable_reference_prices: List[PricePoint]
    reference_prices: List[PricePoint]
    termination_type: TerminationType
