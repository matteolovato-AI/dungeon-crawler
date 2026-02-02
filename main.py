# file principale
from src.models import Room, Map, Entity, Player
from items.item import Item, Potion, Weapon

player = Player("Giocaore", 100,(0,0))

initial_room = Room("Un atrio circolare con pareti di pietra levigata.")
livello = Map(initial_room)
room_2 = Room("Una biblioteca con scaffali rovesciati e pergamene ingiallite.")
dagger = Weapon("Daga rugginosa", 3)
room_2.add_item(dagger)
livello.add_room(room_2,(-1,0))
room_3 = Room("Un balcone naturale che si affaccia su un vuoto oscuro.")
potion = Potion("Pozione di cura", 10)
room_3.add_item(potion)
livello.add_room(room_3, (1, 0))
room_4 = Room("Un corridoio stretto dove l'aria diventa pesante e fredda.")
livello.add_room(room_4, (0, 1))
room_5 = Room("Una stanza con un tavolo da alchimista distrutto.")
room_5.add_item(potion)
livello.add_room(room_5, (2, 0))
room_6 = Room("Un'armeria abbandonata. Odore di ferro e polvere.")
sword = Weapon("Spada corta", 7)
room_6.add_item(sword)
livello.add_room(room_5, (-1,-1))
room_7 = Room("Una cella d'isolamento con catene che pendono dal soffitto.")
room_7.add_item(potion)
livello.add_room(room_7, (-1,-2))
room_8 = Room("Una stanza gelida, le pareti sono coperte da un sottile strato di ghiaccio.")
livello.add_room(room_8, (-1,-3))
room_9 = Room("L'anticamera del Boss, disseminata di scudi spezzati.")
big_potion = Potion("Pozione grande", 50)
room_9.add_item(big_potion)
livello.add_room(room_9, (-1,-4))
room_10 = Room("La sala del trono. Il soffitto è altissimo e l'atmosfera è elettrica.", True)
livello.add_room(room_10, (0,-4))


while True:
    neighbors = livello.check_room_neighbors(player.position)
    print(livello.map[player.position])
    for neighbor in neighbors:
        print(f"Una stanza a {neighbor}")
    
    print("\n\n\nWhat do you want to do?")
    print("1 - Move\n2 - Attack\n3 - Loot item\n4 - Wield item\n5 - Use item")
    scelta = input("Choose 1-5: ").strip()

    if scelta == "1":
        print("Nord, Sud, Est, Ovest")
        direction = input("Dove vuoi andare? ").strip().lower()
        if direction == "nord" and direction in neighbors:
            player.move((player.position[0], player.position[1]+1))
        elif direction == "sud" and direction in neighbors:
            player.move((player.position[0], player.position[1]-1))
        elif direction == "est" and direction in neighbors:
            player.move((player.position[0]+1, player.position[1]))
        elif direction == "ovest" and direction in neighbors:
            player.move((player.position[0]-1, player.position[1]))
        else:
            print("\nPiccolo Harry Potter, quello è un muro, non puoi passare!\n")

    elif scelta == "2":
        pass

    elif scelta == "3":
        pass

    elif scelta == "4":
        pass

    elif scelta == "5":
        pass

    else:
        print("ERROR")
        break