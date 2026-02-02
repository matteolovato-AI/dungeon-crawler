# classi
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

        
   
        
    
