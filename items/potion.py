from items.item import Item

class Potion(Item):
    def __init__(self, name: str, healing_amount: int):
        super().__init__(name)
        self.healing_amount = healing_amount

    def __str__(self):
        return f"{self.name} (Cura: {self.healing_amount})"