# Standard Modules
from typing import Optional, Set

# Local Modules
from cofactr.helpers import get_path


class Seller:
    def __init__(self, seller):
        self._seller = seller

    @property
    def name(self) -> Optional[str]:
        """Best/canonical name of the company."""
        # Prefer label.
        label = get_path(self._seller, ["labels", "en"], None)
        if label:
            return label["value"]

        # Fallback to an alias.
        alias = get_path(self._seller, ["aliases", "en"], [None])[0]
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
