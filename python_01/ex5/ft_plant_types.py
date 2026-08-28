class Plant:
    name: str
    _height: float
    _age_days: int
    growth_rate: float

    def __init__(
        self,
        name: str,
        height: float,
        _age_days: int,
        growth_rate: float = 1.0,
    ) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0
        self.growth_rate = growth_rate
        self.set_height(height)
        self.set_age(_age_days)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, _age_days: int) -> bool:
        if _age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age_days = _age_days
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def grow(self) -> None:
        self._height = self._height + self.growth_rate

    def age(self) -> None:
        self._age_days = self._age_days + 1

    def show(self) -> None:
        height: float

        height = round(self._height, 1)
        print(f"{self.name}: {height}cm, {self._age_days} days old")


class Flower(Plant):
    color: str
    bloomed: bool

    def __init__(
        self,
        name: str,
        height: float,
        _age_days: int,
        color: str,
        growth_rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, _age_days, growth_rate)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    trunk_diameter: float

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float,
        growth_rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        height: float
        diameter: float

        height = round(self.get_height(), 1)
        diameter = round(self.trunk_diameter, 1)
        print(
            f"Tree {self.name} now produces a shade of "
            f"{height}cm long and {diameter}cm wide."
        )

    def show(self) -> None:
        diameter: float

        diameter = round(self.trunk_diameter, 1)
        super().show()
        print(f" Trunk diameter: {diameter}cm")


class Vegetable(Plant):
    harvest_season: str
    nutritional_value: int

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        harvest_season: str,
        growth_rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value = self.nutritional_value + 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    rose: Flower
    oak: Tree
    tomato: Vegetable

    rose = Flower("Rose",ew
￼
42.fr
https://signin.intra.42.fr › password
·
Traduzir esta página
42 logo. Forgot your 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April", 2.1)

    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("")
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("")
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and  age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
        tomato.show()
