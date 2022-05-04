"""Part seller class."""
# Standard Modules
from typing import Optional, Set


class Seller:
    """Part seller."""

    def __init__(self, labels=None, aliases=None, statements=None):
        self._labels = labels
        self._aliases = aliases
        self._statements = statements

    @property
    def name(self) -> Optional[str]:
        """Best/canonical name of the company."""
        # Prefer label.
        label = self._labels.get("en")
        if label:
            return label["value"]

        # Fallback to an alias.
        alias = self._aliases.get("en", [None])[0]
        if alias:
            return alias["value"]

        return None

    @property
    def accuracy_score(self) -> int:
        return 100

    @property
    def quality_score(self) -> int:
        return 100

    @property
    def additional_markup(self) -> float:
        return 0

    @property
    def additional_fee(self) -> float:
        return 0

    @property
    def certifications(self) -> Set[str]:
        return set()

    @property
    def buyable(self) -> bool:
        # There should be an override in the KB. A separate flag
        # for "buyable" that's independent from accuracy.
        return True
