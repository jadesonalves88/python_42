class Plant:
    name: str
    _height: float
    _age_days: int

    def __init__(self, name: str, height: float, _age_days: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(_age_days)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: error , height can't be negative")
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

    def show(self) -> None:
        height: float
        height = round(self._height, 1)
        print(f"{self.name}: {height}cm, {self._age_days} days old")


if __name__ == "__main__":
    rose: Plant

    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System === ")
    print("Plant created: ", end="")
    rose.show()
    print("")

    if rose.set_height(25.0):
        print(f"Height updated: {rose.get_height()}cm")
    else:
        print("Height update rejected")

    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days")
    else:
        print("Age update rejected")

    print("")
    if rose.set_height(-25.0):
        print(f"Height updated: {rose.get_height()}cm")
    else:
        print("Height update rejected")

    if rose.set_age(-10):
        print(f"Age update: {rose.get_age()} days")
    else:
        print("Age update rejected")

    print("")
    print("Current state: ", end="")
    rose.show()
