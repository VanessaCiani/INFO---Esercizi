from typing import override

class Spaceship:
    def __init__(self, name: str):
        self.name = name
        self.speed = 0

    def fly(self):
        print(f"{self.name} sta volando nel vuoo siderale")

    def accellerate(self):
        self.speed += 10
        print(f"{self.name} is accellerating at {self.speed} persec/h")


class CargoShip(Spaceship):
    def __init__(self, name: str, max_load: int):
        super().__init__(name)
        self.max_load = max_load
        self.current_load = 0

class StarFighter(Spaceship):
    @override
    def fly(self):
        print(f"{self.name} sfreccia a velocità di combattimento! Pew Pew!!")

nave_cargo = CargoShip("Nostromo", max_load = 100)
nave_cargo.fly()
nave_cargo.accellerate()
print(f"{nave_cargo.name} va a velocità {nave_cargo.speed}")

nave_combattimento = StarFighter("Millenium Falcon")
nave_combattimento.fly()