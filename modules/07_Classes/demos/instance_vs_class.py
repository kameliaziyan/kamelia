INITIAL_FUEL = 10


class Spaceship:
    def __init__(self, name: str, type: str, fuel_type: str, fuel = INITIAL_FUEL):
        self.name = name
        self.type = type
        self.fuel_type = fuel_type
        self.fuel = fuel

    def refuel(self, amount: int) -> None:
        self.fuel += amount
        print(f"{self.name} has been refueled with {amount}. Current fuel: {self.fuel}")

    @classmethod
    def create_cargo_ship(cls, name: str) -> 'Spaceship':
        return cls(name, "Cargo", "Standard Fuel", 7)

    @classmethod
    def create_battle_ship(cls, name: str) -> 'Spaceship':
        return cls(name, "Battle", "High-Grade Fuel", 50)


if __name__ == "__main__":
    cargo_ship = Spaceship.create_cargo_ship("CargoMaster")
    battle_ship = Spaceship.create_battle_ship("Warrior")

    print(f"{cargo_ship.name} is a {cargo_ship.type} ship with {cargo_ship.fuel} fuel.")
    print(f"{battle_ship.name} is a {battle_ship.type} ship with {battle_ship.fuel} fuel.")

    cargo_ship.refuel(5)
    battle_ship.refuel(20)
