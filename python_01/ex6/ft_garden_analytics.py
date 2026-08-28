class Plant:
    name: str
    _height: float
    _age_days: int
    growth_rate: float
    _stats: "Plant.Stats"

    class Stats:
        _grow_count: int
        _age_count: int
        _show_count: int

        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def add_grow(self) -> None:
            self._grow_count = self._grow_count + 1

        def add_age(self) -> None:
            self._age_count = self._age_count + 1
ew
￼
42.fr
https://signin.intra.42.fr › password
·
Traduzir esta página
42 logo. Forgot your
        def add_show(self) -> None:
            self._show_count = self._show_count + 1

        def show(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth_rate: float = 1.0,
    ) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0
        self.growth_rate = growth_rate
        self._stats = Plant.Stats()
        self.set_height(height)
        self.set_age(age_days)

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age_days: int) -> bool:
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age_days = age_days
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def grow(self) -> None:
        self._height = self._height + self.growth_rate
        self._stats.add_grow()

    def age(self, days: int = 1) -> None:
        self._age_days = self._age_days + days
        self._stats.add_age()

    def show(self) -> None:
        height: float

        self._stats.add_show()
        height = round(self._height, 1)
        print(f"{self.name}: {height}cm, {self._age_days} days old")

    def show_stats(self) -> None:
        self._stats.show()


class Flower(Plant):
    color: str
    bloomed: bool

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
        growth_rate: float = 1.0,
    ) -> None:
        super()._ew
￼
42.fr
https://signin.intra.42.fr › password
·
Traduzir esta página
42 logo. Forgot your_init__(name, height, age_days, growth_rate)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    trunk_diameter: float
    _shade_count: int

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
        self._shade_count = 0

    def produce_shade(self) -> None:
        height: float
        diameter: float

        height = round(self.get_height(), 1)
        diameter = round(self.trunk_diameter, 1)
        print(
            f"Tree {self.name} now produces a shade of "
            f"{height}cm long and {diameter}cm wide."
        )
        self._shade_count = self._shade_count + 1

    def show(self) -> None:
        diameter: float

        diameter = round(self.trunk_diameter, 1)
        super().show()
        print(f" Trunk diameter: {diameter}cm")

    def show_stats(self) -> None:
        super().show_stats()
        print(f" {self._shade_count} shade")


class Seed(Flower):
    _seed_amount: int
    _seeds: intew
￼
42.fr
https://signin.intra.42.fr › password
·
Traduzir esta página
42 logo. Forgot your

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
        seed_amount: int,
        growth_rate: float = 1.0
    ) -> None:
        super().__init__(name, height, age_days, color, growth_rate)
        self._seed_amount = seed_amount
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = self._seed_amount

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

ew
￼
42.fr
https://signin.intra.42.fr › password
·
Traduzir esta página
42 logo. Forgot your
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


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


def main() -> None:
    rose: Flower
    oak: Tree
    sunflower: Seed
    anonymous: Plant
    is_old: bool

    rose = Flower("Rose", 15.0, 10, "red", 8.0)
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42, 30.0)
    anonymous = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    is_old = Plant.is_older_than_year(30)
    print(f"Is 30 days more than a year? -> {is_old}")
    is_old = Plant.is_older_than_year(400)
    print(f"Is 400 days more than a year? -> {is_old}")

    print("")
    print("=== Flower")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("")
    print("=== Tree")
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("")
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("")
    print("=== Anonymous")
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
