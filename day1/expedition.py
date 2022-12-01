from elf import Elf


class Expedition:
    def __init__(self):
        self.elves = []

    def load_elves_from_file(self, file) -> None:
        with open(file) as f:
            elf = Elf()

            for line in f:
                if line.strip() == '':
                    self.add_elf_to_expedition(elf)
                    elf = Elf()
                else:
                    elf.add_to_inventory(int(line))

    def add_elf_to_expedition(self, elf: Elf) -> None:
        self.elves.append(elf)

    def elf_with_most_calories(self) -> Elf:
        return self.elves_sorted_by_inventory_calories()[0]

    def sum_calories_for_top_elves(self) -> int:
        return sum([elf.total_calories_of_inventory() for elf in self.elves_sorted_by_inventory_calories()[:3]])

    def elves_sorted_by_inventory_calories(self) -> list[Elf]:
        return sorted(self.elves, key=lambda elf: elf.total_calories_of_inventory(), reverse=True)
