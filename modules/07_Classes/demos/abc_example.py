from abc import ABC, abstractmethod


class AbstractSpaceShip(ABC):

    def greet(self) -> None:
        print("Welcome aboard the spaceship!")

    @abstractmethod
    def launch(self) -> None:
        """ Launch the spaceship. """

    @abstractmethod
    def land(self) -> None:
        """ Land the spaceship. """


class CargoShip(AbstractSpaceShip):
    def launch(self) -> None:
        print("Cargo ship launching...")

    def land(self) -> None:
        print("Cargo ship landing...")


def operate_space_ship(ship: AbstractSpaceShip) -> None:
    ship.launch()
    ship.land()
    ship.greet()


if __name__ == "__main__":
    cargo_ship = CargoShip()
    operate_space_ship(cargo_ship)
