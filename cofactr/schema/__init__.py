"""Schema definitions."""
# Standard Modules
from enum import Enum
from typing import Callable, Dict

# Local Modules
from cofactr.helpers import identity
from cofactr.schema.flagship import FlagshipOffer, FlagshipPart, FlagshipSeller
from cofactr.schema.flagship_v2 import FlagshipV2Offer, FlagshipV2Part, FlagshipV2Seller
from cofactr.schema.flagship_v3 import FlagshipV3Offer, FlagshipV3Part, FlagshipV3Seller
from cofactr.schema.flagship_v4 import FlagshipV4Part, FlagshipV4Offer, FlagshipV4Seller
from cofactr.schema.flagship_v5 import FlagshipV5Offer, FlagshipV5Part
from cofactr.schema.flagship_v6 import FlagshipV6Part
from cofactr.schema.flagship_v7 import FlagshipV7Part
from cofactr.schema.flagship_alts_v0 import FlagshipAltsV0Part
from cofactr.schema.flagship_cache_v0 import FlagshipCacheV0Part
from cofactr.schema.flagship_cache_v1 import FlagshipCacheV1Part
from cofactr.schema.flagship_cache_v2 import FlagshipCacheV2Part
from cofactr.schema.flagship_cache_v3 import FlagshipCacheV3Part
from cofactr.schema.flagship_cache_v4 import FlagshipCacheV4Part
from cofactr.schema.logistics import LogisticsOffer, LogisticsPart
from cofactr.schema.logistics_v2 import (
    LogisticsV2Part,
    LogisticsV2Offer,
    LogisticsV2Seller,
)
from cofactr.schema.logistics_v3 import LogisticsV3Part
from cofactr.schema.logistics_v4 import LogisticsV4Part
from cofactr.schema.price_solver_v0 import PriceSolverV0Part
from cofactr.schema.price_solver_v1 import PriceSolverV1Part
from cofactr.schema.price_solver_v2 import PriceSolverV2Part
from cofactr.schema.price_solver_v3 import PriceSolverV3Part
from cofactr.schema.price_solver_v4 import PriceSolverV4Part
from cofactr.schema.price_solver_v5 import PriceSolverV5Part
from cofactr.schema.price_solver_v6 import PriceSolverV6Part
from cofactr.schema.price_solver_v7 import PriceSolverV7Part


class ProductSchemaName(str, Enum):
    """Product schema name."""

    INTERNAL = "internal"
    FLAGSHIP = "flagship"
    FLAGSHIP_V2 = "flagship-v2"
    FLAGSHIP_V3 = "flagship-v3"
    FLAGSHIP_V4 = "flagship-v4"
    FLAGSHIP_V5 = "flagship-v5"
    FLAGSHIP_V6 = "flagship-v6"
    FLAGSHIP_V7 = "flagship-v7"
    FLAGSHIP_ALTS_V0 = "flagship-alts-v0"
    FLAGSHIP_CACHE_V0 = "flagship-cache-v0"
    FLAGSHIP_CACHE_V1 = "flagship-cache-v1"
    FLAGSHIP_CACHE_V2 = "flagship-cache-v2"
    FLAGSHIP_CACHE_V3 = "flagship-cache-v3"
    FLAGSHIP_CACHE_V4 = "flagship-cache-v4"
    LOGISTICS = "logistics"
    LOGISTICS_V2 = "logistics-v2"
    LOGISTICS_V3 = "logistics-v3"
    LOGISTICS_V4 = "logistics-v4"
    PRICE_SOLVER_V0 = "price-solver-v0"
    PRICE_SOLVER_V1 = "price-solver-v1"
    PRICE_SOLVER_V2 = "price-solver-v2"
    PRICE_SOLVER_V3 = "price-solver-v3"
    PRICE_SOLVER_V4 = "price-solver-v4"
    PRICE_SOLVER_V5 = "price-solver-v5"
    PRICE_SOLVER_V6 = "price-solver-v6"
    PRICE_SOLVER_V7 = "price-solver-v7"


schema_to_product: Dict[ProductSchemaName, Callable] = {
    ProductSchemaName.FLAGSHIP: FlagshipPart,
    ProductSchemaName.FLAGSHIP_V2: FlagshipV2Part,
    ProductSchemaName.FLAGSHIP_V3: FlagshipV3Part,
    ProductSchemaName.FLAGSHIP_V4: FlagshipV4Part,
    ProductSchemaName.FLAGSHIP_V5: FlagshipV5Part,
    ProductSchemaName.FLAGSHIP_V6: FlagshipV6Part,
    ProductSchemaName.FLAGSHIP_V7: FlagshipV7Part,
    ProductSchemaName.FLAGSHIP_ALTS_V0: FlagshipAltsV0Part,
    ProductSchemaName.FLAGSHIP_CACHE_V0: FlagshipCacheV0Part,
    ProductSchemaName.FLAGSHIP_CACHE_V1: FlagshipCacheV1Part,
    ProductSchemaName.FLAGSHIP_CACHE_V2: FlagshipCacheV2Part,
    ProductSchemaName.FLAGSHIP_CACHE_V3: FlagshipCacheV3Part,
    ProductSchemaName.FLAGSHIP_CACHE_V4: FlagshipCacheV4Part,
    ProductSchemaName.LOGISTICS: LogisticsPart,
    ProductSchemaName.LOGISTICS_V2: LogisticsV2Part,
    ProductSchemaName.LOGISTICS_V3: LogisticsV3Part,
    ProductSchemaName.LOGISTICS_V4: LogisticsV4Part,
    ProductSchemaName.PRICE_SOLVER_V0: PriceSolverV0Part,
    ProductSchemaName.PRICE_SOLVER_V1: PriceSolverV1Part,
    ProductSchemaName.PRICE_SOLVER_V2: PriceSolverV2Part,
    ProductSchemaName.PRICE_SOLVER_V3: PriceSolverV3Part,
    ProductSchemaName.PRICE_SOLVER_V4: PriceSolverV4Part,
    ProductSchemaName.PRICE_SOLVER_V5: PriceSolverV5Part,
    ProductSchemaName.PRICE_SOLVER_V6: PriceSolverV6Part,
    ProductSchemaName.PRICE_SOLVER_V7: PriceSolverV7Part,
}


class OfferSchemaName(str, Enum):
    """Offer schema name."""

    INTERNAL = "internal"
    FLAGSHIP = "flagship"
    FLAGSHIP_V2 = "flagship-v2"
    FLAGSHIP_V3 = "flagship-v3"
    FLAGSHIP_V4 = "flagship-v4"
    FLAGSHIP_V5 = "flagship-v5"
    LOGISTICS = "logistics"
    LOGISTICS_V2 = "logistics-v2"


schema_to_offer: Dict[OfferSchemaName, Callable] = {
    OfferSchemaName.INTERNAL: identity,
    OfferSchemaName.FLAGSHIP: FlagshipOffer,
    OfferSchemaName.FLAGSHIP_V2: FlagshipV2Offer,
    OfferSchemaName.FLAGSHIP_V3: FlagshipV3Offer,
    OfferSchemaName.FLAGSHIP_V4: FlagshipV4Offer,
    OfferSchemaName.FLAGSHIP_V5: FlagshipV5Offer,
    OfferSchemaName.LOGISTICS: LogisticsOffer,
    OfferSchemaName.LOGISTICS_V2: LogisticsV2Offer,
}


class OrgSchemaName(str, Enum):
    """Organization schema name."""

    INTERNAL = "internal"
    FLAGSHIP = "flagship"
    FLAGSHIP_V2 = "flagship-v2"
    FLAGSHIP_V3 = "flagship-v3"
    FLAGSHIP_V4 = "flagship-v4"
    LOGISTICS = "logistics"
    LOGISTICS_V2 = "logistics-v2"


schema_to_org: Dict[OrgSchemaName, Callable] = {
    OrgSchemaName.INTERNAL: identity,
    OrgSchemaName.FLAGSHIP: FlagshipSeller,
    OrgSchemaName.FLAGSHIP_V2: FlagshipV2Seller,
    OrgSchemaName.FLAGSHIP_V3: FlagshipV3Seller,
    OrgSchemaName.FLAGSHIP_V4: FlagshipV4Seller,
    OrgSchemaName.LOGISTICS: FlagshipSeller,
    OrgSchemaName.LOGISTICS_V2: LogisticsV2Seller,
}


class SupplierSchemaName(str, Enum):
    """Supplier schema name."""

    INTERNAL = "internal"
    FLAGSHIP = "flagship"
    FLAGSHIP_V2 = "flagship-v2"
    FLAGSHIP_V3 = "flagship-v3"
    FLAGSHIP_V4 = "flagship-v4"
    LOGISTICS = "logistics"
    LOGISTICS_V2 = "logistics-v2"


schema_to_supplier: Dict[SupplierSchemaName, Callable] = {
    SupplierSchemaName.INTERNAL: identity,
    SupplierSchemaName.FLAGSHIP: FlagshipSeller,
    SupplierSchemaName.FLAGSHIP_V2: FlagshipV2Seller,
    SupplierSchemaName.FLAGSHIP_V3: FlagshipV3Seller,
    SupplierSchemaName.FLAGSHIP_V4: FlagshipV4Seller,
    SupplierSchemaName.LOGISTICS: FlagshipSeller,
    SupplierSchemaName.LOGISTICS_V2: LogisticsV2Seller,
}
