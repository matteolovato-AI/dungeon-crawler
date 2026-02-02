# classi
from items.item import Item,Potion,Weapon

class Entity:
    def __init__(self, name: str, health: int,damage:int=0):
        self.name = name
        self.health = health
        self.damage=damage
    
    def health_amount(self, damage: int) -> int:
         self.health = (self.health) - damage
         
         if(self.health<0):
             self.health=0
         return self.health

class Player(Entity):
    def __init__(self, name: str, health: int, position:tuple[int,int]):
        super().__init__(name, health,damage=1)
        self.position = position
        self.inventory = []
        self.equipped_weapon = None
    
    def move(self, new_position: tuple[int, int]):
        self.position = new_position
    
    def pick_up_item(self, item: Item):
        self.inventory.append(item)
        print(f"You put {item.name} in your inventory.")

    def equip_weapon(self, weapon: Weapon):
        if weapon in self.inventory:
            self.equipped_weapon = weapon
            self.damage = weapon.damage
            print(f"You have equipped {weapon.name}. Damage: {self.damage}")
        else:
            print("You don't have this weapon in your inventory!")
    
    def use_potion(self, potion: Potion):
        if potion in self.inventory:
            current_hp =(self.health)
            
            self.health = (current_hp + potion.healing_amount)
        
            self.inventory.remove(potion)

            if self.health > 100:
                self.health = 100
            print(f"You have used {potion.name}. Current HP: {self.health}")

        
        


        
   
        
    
class Room:
    def __init__(self, description, boss=False) -> None:
        self.description = description
        self.items: list[Item] = []
        self.enemies: list[Entity] = []
        self.boss = boss
    def add_item(self, item: Item):
        self.items.append(item)
    def add_enemy(self, enemy: Entity):
        self.enemies.append(enemy)
    def __str__(self) -> str:
        return self.description

class Map:
    def __init__(self, room: Room) -> None:
        # creo la mappa con la prima stanza come inizio
        self.map = {(0,0): room}
        pass
    def add_room(self, room: Room, room_position: tuple[int,int]) -> None:
        self.map[room_position] = room
    def check_room_neighbor_direction(self, position, direction) -> bool:

        target_x, target_y = position[0], position[1]
        if direction == "nord":
            target_y += 1
        elif direction == "sud":
            target_y -= 1
        elif direction == "est":
            target_x += 1
        elif direction == "ovest":
            target_x -= 1
        # ritorna la posizione della stanza adiacente
        return True if (target_x, target_y) in self.map.keys() else False

    def check_room_neighbors(self, position) -> list[tuple[int,int]]:
            neighbors = []
            for dir in ['nord', 'sud', 'est', 'ovest']:
                is_neighbor = self.check_room_neighbor_direction(position, dir)
                if is_neighbor:
                    neighbors.append(dir)

            return neighbors
