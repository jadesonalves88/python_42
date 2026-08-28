import sys


def main() -> None:
    args: list[str] = sys.argv[1:]
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    seen: set[str] = set()

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        parts: list[str] = arg.split(":", 1)
        name: str = parts[0]
        qty_str: str = parts[1]

        if name in seen:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty: int = int(qty_str)
        except ValueError:
            print(
                f"Quantity error for '{name}': "
                f"invalid literal for int() with base 10: '{qty_str}'"
            )
            continue

        inventory[name] = qty
        seen.add(name)

    print(f"Got inventory: {inventory}")

    if len(inventory) == 0:
        return

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty: int = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_qty}")

    if total_qty == 0:
        return

    for item_name in item_list:
        pct: float = (inventory[item_name] / total_qty) * 100
        print(f"Item {item_name} represents {round(pct, 1)}%")

    max_qty: int = max(inventory.values())
    min_qty: int = min(inventory.values())
    most_abundant: str = ""
    least_abundant: str = ""
    for item_name in item_list:
        if inventory[item_name] == max_qty and most_abundant == "":
            most_abundant = item_name
        if inventory[item_name] == min_qty and least_abundant == "":
            least_abundant = item_name

    print(
        f"Item most abundant: {most_abundant} with quantity {max_qty}"
    )
    print(
        f"Item least abundant: {least_abundant} with quantity {min_qty}"
    )

    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
