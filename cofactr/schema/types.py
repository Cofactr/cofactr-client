"""Types for use in schema definitions."""
# Standard Modules
from typing import Any, Literal, Optional, TypedDict


class OfferCorrection(TypedDict):
    """Offer correction."""

    correct_value: Any
    original_value: Any
    detail: Optional[str]
    created_at: str


class Document(TypedDict):
    """Document."""

    label: str
    url: str
    filename: str


class Completion(TypedDict):
    """Autocomplete prediction."""

    id: str
    label: str


TerminationType = Literal[
    "other",
    "SMT",
    "THT",
    "pressed fit",
    "hybrid of SMT and THT",
    "hybrid of pressed fit and SMT",
    "hybrid of pressed fit and THT",
]
