class Item:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

#weapon
class Weapon(Item):
    def __init__(self, name: str, damage: int):
        super().__init__(name)
        self.damage = damage

    def __str__(self):
        return f"{self.name} (Danno: {self.damage})"

#potion
class Potion(Item):
    def __init__(self, name: str, healing_amount: int):
        super().__init__(name)
        self.healing_amount = healing_amount

    def __str__(self):
        return f"{self.name} (Cura: {self.healing_amount})"