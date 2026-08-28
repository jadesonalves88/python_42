class Plant:
    name: str
    height: float
    age_days: int
    growth_rate: float

    def show(self) -> None:
        height: float
        height = round(self.height, 1)
        print(f"{self.name}: {height}cm, {self.age_days} days old")

    def grow(self) -> None:
        self.height = self.height + self.growth_rate

    def age(self) -> None:
        self.age_days = self.age_days + 1


if __name__ == "__main__":
    rose: Plant = Plant()
    start_height: float
    total_growth: float

    rose.name = "Rose"
    rose.height = 25.0
    rose.age_days = 30
    rose.growth_rate = 0.5

    start_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

        total_growth = round(rose.height - start_height, 1)
        print(f"Growth this week: {total_growth}cm")
