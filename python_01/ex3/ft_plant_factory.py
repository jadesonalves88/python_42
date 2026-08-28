class Plant:
    name: str
    height: float
    age_days: int
    growth_rate: float

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth_rate: float = 1.0,
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        height: float
        height = round(self.height, 1)
        print(f"{self.name}: {height}cm, {self.age_days} day old")

    def grow(self) -> None:
        self.height = self.height + self.growth_rate

    def age(self) -> None:
        self.age_days = self.age_days + 1


if __name__ == "__main__":
    plants: list[Plant]

    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    for p in plants:
        print("Created: ", end="")
        p.show()
