"""Types for use in schema definitions."""
# Standard Modules
from typing import Any, List, Literal, Optional, TypedDict
from typing_extensions import NotRequired


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


LifecycleStatusType = Literal[
    "New",
    "NRFND",
    "Production",
    "EOL",
    "Obsolete",
]
TerminationType = Literal[
    "other",
    "SMT",
    "THT",
    "pressed fit",
    "hybrid of SMT and THT",
    "hybrid of pressed fit and SMT",
    "hybrid of pressed fit and THT",
]

class ManufacturerInV0(TypedDict):
    """Manufacturer input."""

    custom_label: NotRequired[Optional[str]]
    custom_id: NotRequired[Optional[str]]
    id: NotRequired[Optional[str]]


class ClassificationInV0(TypedDict):
    """Classification input."""

    custom_label: NotRequired[Optional[str]]
    custom_id: NotRequired[Optional[str]]
    id: NotRequired[Optional[str]]


class PartInV0(TypedDict):
    """Part input."""

    owner_id: str

    mpn: str
    alt_mpns: NotRequired[Optional[List[str]]]
    custom_id: NotRequired[Optional[str]]
    mfr: NotRequired[Optional[ManufacturerInV0]]

    classification: NotRequired[Optional[ClassificationInV0]]
    description: NotRequired[Optional[str]]
    msl: NotRequired[Optional[str]]
    package: NotRequired[Optional[str]]
    terminations: NotRequired[Optional[int]]
    termination_type: NotRequired[Optional[TerminationType]]

class PartialPartInV0(TypedDict):
    """Partial part input."""

    owner_id: NotRequired[Optional[str]]

    mpn: NotRequired[Optional[List[str]]]
    alt_mpns: NotRequired[Optional[List[str]]]
    custom_id: NotRequired[Optional[str]]
    mfr: NotRequired[Optional[ManufacturerInV0]]

    classification: NotRequired[Optional[ClassificationInV0]]
    description: NotRequired[Optional[str]]
    lifecycle_status: NotRequired[Optional[LifecycleStatusType]]
    msl: NotRequired[Optional[str]]
    package: NotRequired[Optional[str]]
    terminations: NotRequired[Optional[int]]
    termination_type: NotRequired[Optional[TerminationType]]


class ScheduledReleaseV0(TypedDict):
    """Scheduled release."""

    scheduled_date: Optional[str]  # Datetime.
    scheduled_quantity: Optional[int]


class OrderLineInV0(TypedDict):
    """Order line input."""

    customer_reference: str
    cofactr_product_id: str
    seller_product_id: str
    quantity_ordered: int
    # Expected unit price. This is required so any discrepancies between between the expected and
    # actual price can be addressed.
    expected_unit_price: float
    schedule: List[ScheduledReleaseV0]


class PostalAddressV0(TypedDict):
    """Postal Address."""

    # The country (Ex: `"USA"`). You can also provide the two-letter ISO 3166-1 alpha-2 country
    # code (Ex: `"US"`).
    country: str
    # The region in which the locality is, and which is in the country (Ex: `"California"` or
    # another appropriate first-level Administrative division).
    region: str
    # The locality in which the street address is, and which is in the region
    # (Ex: `"Mountain View"`).
    locality: str
    # The postal code (Ex: `"94043"`).
    postal_code: str
    # Attention line (Ex: `"Engineering Department"`).
    attention_line: NotRequired[Optional[str]]
    # Street address line one (Ex: `"1000 Main Street"`).
    street_address_line_one: str
    # Street address line two (Ex: `"Suite 300"`).
    street_address_line_two: NotRequired[Optional[str]]


class ContactV0(TypedDict):
    """Contact."""

    # Customer ID in seller's system.
    seller_customer_id: str
    company: str
    first_name: str
    last_name: str
    telephone: str
    email: str
    address: PostalAddressV0


class OrderInV0(TypedDict):
    """Order input."""

    # Order owner, which dictates what configuration will be used to place the order. If it is
    # `None` or not provided, Cofactr's own distributor accounts and configuration will be used.
    # If an ID is provided that doesn't have configuration set up, an error will be returned.
    owner_id: NotRequired[Optional[str]]

    # Seller ID.
    seller_id: str
    # Purchase order number.
    po_number: str
    buyer_contact: ContactV0
    shipping_contact: ContactV0
    # Billing account ID (Example: Digi-Key Net Terms Billing account number). If it is `None`
    # or not provided, the fall back will be the default set up in integration-wide configuration.
    billing_account_id: NotRequired[Optional[str]]
    shipment_grouping_preference: Literal["unspecified", "as-available", "min-shipments"]
    # Shipping methods in order of preference (Example: `["FedEx Ground"]`).
    shipping_methods: List[str]
    order_lines: List[OrderLineInV0]
