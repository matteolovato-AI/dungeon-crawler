# classi
from ..items.item import Item

class Entity:
    def __init__(self, name: str, health: str,damage:int=0):
        self.name = name
        self.health = health
        self.damage=damage
    
    def health_amount(self, damage: int) -> int:
         self.health = int(self.health) - damage
         
         if(self.health<0):
             self.health=0
         return self.health

class Player(Entity):
    def __init__(self, name: str, health: str, position:tuple[int,int]):
        super().__init__(name, health)
        self.position = position

        
   
        
    
class Room:
    def __init__(self, description) -> None:
        self.description = description
        self.items: list[Item] = []
        self.enemies: list[Entity] = []
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
    def check_room_neighbor_direction(self, position, direction) -> tuple[int,int] | None:

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
        return (target_x, target_y) if (target_x >= 0 and target_y >= 0) else None

    def check_room_neighbors(self, position) -> list[tuple[int,int]]:
        neighbors = []
        neighbors.append(self.check_room_neighbor_direction(position, 'nord'))
        neighbors.append(self.check_room_neighbor_direction(position, 'sud'))
        neighbors.append(self.check_room_neighbor_direction(position, 'est'))
        neighbors.append(self.check_room_neighbor_direction(position, 'ovest'))
        return neighbors
