from typing import Protocol
from typing import Union


class SpaceShipProtocol(Protocol):
    def launch(self) -> None:
        """Launch the spaceship."""
        ...


class LandableProtocol(Protocol):
    def land(self) -> None:
        """Land the spaceship."""
        ...


class CargoShip(SpaceShipProtocol, LandableProtocol):
    def launch(self) -> None:
        print("Cargo ship launching...")

    def land(self) -> None:
        print("Cargo ship landing...")


def operate_space_ship(ship: Union[SpaceShipProtocol, LandableProtocol]) -> None:
    ship.launch()
    ship.land()


if __name__ == "__main__":
    cargo_ship = CargoShip()
    operate_space_ship(cargo_ship)
