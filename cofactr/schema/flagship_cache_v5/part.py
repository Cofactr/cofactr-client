"""Part class."""
# Standard Modules
from dataclasses import dataclass

# Local Modules
from cofactr.schema.flagship_cache_v4.part import Part as FlagshipCacheV4Part


@dataclass
class Part(FlagshipCacheV4Part):  # pylint: disable=too-many-instance-attributes
    """Part."""

    msl: str
