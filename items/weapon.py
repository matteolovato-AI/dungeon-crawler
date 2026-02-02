from items.item import Item

class Weapon(Item):
    def __init__(self, name: str, damage: int):
        super().__init__(name)
        self.damage = damage

    def __str__(self):
        return f"{self.name} (Danno: {self.damage})"
