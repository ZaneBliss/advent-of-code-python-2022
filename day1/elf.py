class Elf:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, food: int) -> None:
        self.inventory.append(food)

    def total_calories_of_inventory(self) -> int:
        return sum(self.inventory)

    def __str__(self):
        return f'Elf(id={id(self)}, inventory={self.inventory})'
