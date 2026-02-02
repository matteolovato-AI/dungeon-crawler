# file principale
from src.models import Room, Map, Entity, Player
from items.item import Item, Potion, Weapon

initial_room = Room("Stanza iniziale")
map = Map(initial_room)
room_2 = Room("Seconda stanza")
map.add_room(room_2,(1,0))
room_3 = Room("Terza stanza")
map.add_room(room_3, (0,1))
room_4 = Room("quarta stanza")
map.add_room(room_4, (0,-1))
room_5 = Room("Quinta stanza")
map.add_room(room_5, (0,-2))
room_6 = Room("Sesta stanza")
map.add_room(room_5, (-1,-1))
room_7 = Room("Settima stanza")
map.add_room(room_7, (-1,-2))
room_8 = Room("Ottava stanza")
map.add_room(room_8, (-1,-3))
room_9 = Room("Nova stanza")
map.add_room(room_9, (-1,-4))
room_10 = Room("Boss stanza")
map.add_room(room_10, (0,-4))


while True:
    
    
    print("\n\n\nWhat do you want to do?")
    print("1 - Move\n2 - Attack\n3 - Loot item\n4 - Wield item\n5 - Use item")
    scelta = input("Choose 1-5: ").strip()

    if scelta == "1":
        pass

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