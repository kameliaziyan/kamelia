from __future__ import annotations
from typing import Protocol

ZERO_FLOAT: float = float(0)
PERCENT_DIVISOR: int = 100


class Item:
    def __init__(self, name: str, base_price: float, weight: float) -> None:
        self.name = name
        self.base_price = base_price
        self.weight = weight

    def get_info(self) -> str:
        return (
            f"Item: {self.name}, "
            f"Price: ${self.base_price:.2f}, "
            f"Weight: {self.weight:.2f}kg"
        )


class _DiscountProtocol(Protocol):
    base_price: float
    discount_percent: float


class _ShippingProtocol(Protocol):
    weight: float
    shipping_rate_per_kg: float


class DiscountMixin:
    def __init__(self, discount_percent: float = ZERO_FLOAT) -> None:
        self.discount_percent = discount_percent

    def get_price(self: _DiscountProtocol) -> float:
        discount_amount = self.base_price * (self.discount_percent / PERCENT_DIVISOR)
        return self.base_price - discount_amount


class ShippingMixin:
    shipping_rate_per_kg: float = 5.0

    def get_shipping_cost(self: _ShippingProtocol) -> float:
        return self.weight * self.shipping_rate_per_kg


class Product(Item, DiscountMixin, ShippingMixin):
    def __init__(
        self,
        name: str,
        base_price: float,
        weight: float,
        discount_percent: float = ZERO_FLOAT,
    ) -> None:
        Item.__init__(self, name, base_price, weight)
        DiscountMixin.__init__(self, discount_percent)

    def get_total_cost(self) -> float:
        return self.get_price() + self.get_shipping_cost()

    def get_info(self) -> str:
        price = self.get_price()
        shipping = self.get_shipping_cost()
        total = self.get_total_cost()

        return (
            f"Product: {self.name}, "
            f"Price: ${price:.2f}, "
            f"Shipping: ${shipping:.2f}, "
            f"Total: ${total:.2f}"
        )


class DigitalProduct(Item, DiscountMixin):
    def __init__(
        self,
        name: str,
        base_price: float,
        discount_percent: float = ZERO_FLOAT,
    ) -> None:
        Item.__init__(self, name, base_price, weight=ZERO_FLOAT)
        DiscountMixin.__init__(self, discount_percent)

    def get_info(self) -> str:
        price = self.get_price()
        return f"Digital Product: {self.name}, " f"Price: ${price:.2f} (no shipping)"
