"""Part class."""
# Standard Modules
from dataclasses import dataclass
from typing import Optional

# Local Modules
from cofactr.schema.flagship.part import Part as FlagshipPart


@dataclass
class Part(FlagshipPart):  # pylint: disable=too-many-instance-attributes
    """Part."""

    mount_type: Optional[str]
