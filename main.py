# file principale
from time import sleep
from src.models import Room, Map, Entity, Player
from items.item import Item, Potion, Weapon

player = Player("Giocatore", 100,(0,0))

initial_room = Room("Un atrio circolare con pareti di pietra levigata.")
livello = Map(initial_room)
room_2 = Room("Una biblioteca con scaffali rovesciati e pergamene ingiallite.")
dagger = Weapon("Daga rugginosa", 3)
room_2.add_item(dagger)
livello.add_room(room_2,(-1,0))
room_3 = Room("Un balcone naturale che si affaccia su un vuoto oscuro.")
potion = Potion("Pozione di cura", 10)
room_3.add_item(potion)
giant_mouse = Entity("Topo gigante", health=3, damage=1)
giant_mouse2 = Entity("Topo gigante", health=3, damage=1)
room_3.add_enemy(giant_mouse)
room_3.add_enemy(giant_mouse2)
livello.add_room(room_3, (1, 0))
room_4 = Room("Un corridoio stretto dove l'aria diventa pesante e fredda.")
skeleton = Entity("Scheletro errante", health=5, damage=3)
room_4.add_enemy(skeleton)
livello.add_room(room_4, (0, 1))
room_5 = Room("Una stanza con un tavolo da alchimista distrutto.")
potion1 = Potion("Pozione di cura", 10)
room_5.add_item(potion1)
livello.add_room(room_5, (2, 0))
room_6 = Room("Un'armeria abbandonata. Odore di ferro e polvere.")
spider = Entity("Ragno delle grotte", health=4, damage=5)
room_6.add_enemy(spider)
sword = Weapon("Spada corta", 8)
room_6.add_item(sword)
livello.add_room(room_6, (-1,-1))
room_7 = Room("Una cella d'isolamento con catene che pendono dal soffitto.")
shadow = Entity("Ombra corrotta", health=4, damage=10)
room_7.add_enemy(shadow)
potion2 = Potion("Pozione di cura", 10)
room_7.add_item(potion2)
livello.add_room(room_7, (-1,-2))
room_8 = Room("Una stanza gelida, le pareti sono coperte da un sottile strato di ghiaccio.")
livello.add_room(room_8, (-1,-3))
room_9 = Room("L'anticamera del Boss, disseminata di scudi spezzati.")
guard = Entity("Guardia scelta", health=20, damage=5)
big_potion = Potion("Pozione grande", 50)
room_9.add_item(big_potion)
livello.add_room(room_9, (-1,-4))
room_10 = Room("La sala del trono. Il soffitto è altissimo e l'atmosfera è elettrica.", boss=True)
boss = Entity("Il signore delle Ossa", health=40, damage=8)
room_10.add_enemy(boss)
livello.add_room(room_10, (0,-4))


while True:
    print("")
    print(player)
    neighbors = livello.check_room_neighbors(player.position)
    current_room = livello.map[player.position]
    print(current_room)
    for neighbor in neighbors:
        print(f"Una stanza a {neighbor}")
    curret_room_enemies_number = len(current_room.enemies)
    if curret_room_enemies_number:
        print(f"Ci sono {curret_room_enemies_number} nemici!")
    for index, enemy in enumerate(current_room.enemies):
        print(index+1, '-', enemy)
    

    print("\n\nWhat do you want to do?")
    print("1 - Move\n2 - Attack\n3 - Loot item\n4 - Wield item\n5 - Use item")
    scelta = input("Choose 1-5: ").strip()

    if scelta == "1":
        print("Nord, Sud, Est, Ovest")
        direction = input("Dove vuoi andare? ").strip().lower()
        # chiedo la direzione e mi sposto se la direzione è valida e se nella stanza corrente non ci sono nemici
        if direction == "nord" and direction in neighbors and not curret_room_enemies_number:
            player.move((player.position[0], player.position[1]+1))
        elif direction == "sud" and direction in neighbors and not curret_room_enemies_number:
            player.move((player.position[0], player.position[1]-1))
        elif direction == "est" and direction in neighbors and not curret_room_enemies_number:
            player.move((player.position[0]+1, player.position[1]))
        elif direction == "ovest" and direction in neighbors and not curret_room_enemies_number:
            player.move((player.position[0]-1, player.position[1]))
        else:
            print("-"*40)
            if curret_room_enemies_number:
                print("Ci sono dei nemici, non puoi scappare! ")
            else:
                print("Piccolo Harry Potter, quello è un muro, non puoi passare!")
            print("-"*40)

    elif scelta == "2":
        if curret_room_enemies_number:
            # ci sono nemici nella stanza
            print("\nCi sono nemici nella stanza")
            for enemy_index, enemy in enumerate(current_room.enemies):
                print(enemy_index+1, "-", enemy)
            enemy_index = int(input("Quale nemico vuoi colpire? ").strip()) - 1
            # colpisce il nemico e lo rimuove dalla lista se muore
            current_room.hit_enemy(enemy_index, player.damage)
            # se muore il nemico viene rimosso, ricalcolo il numero di nemiri nella stanza
            curret_room_enemies_number = len(current_room.enemies)
            if current_room.boss and not curret_room_enemies_number:
                print("Il tesoro non ha più un guardiano, ora è tutto tuo")
                sleep(1)
                print("L'affatticamento dalla battaglia e le ferite riportate ti spingono")
                sleep(1)
                print("a riposarti, l'emozione del tesoro e l'adrenalina dell'ultima")
                sleep(1)
                print("battaglia, vogliono che continui...")
                sleep(1)
                print("Tutto un colpo non ti senti molto bene.. Collassi a terra e muori")
                sleep(1)
                print("...")
                sleep(1)
                print("...")
                sleep(1)
                print("...")
                sleep(1)
                print("FINE")
                break
        else:
            # non ci sono nemici nella stanza
            print("-"*40)
            print("Hai cercato di colpire il vuoto...")
            print("Sei inciampato")
            sleep(1)
            print("Nessuno ha visto nulla!")
            print("-"*40)

    elif scelta == "3":
        print("Cercando oggetti..")
        current_room_objects_number = len(current_room.items)
        if current_room_objects_number:
            print(f"Ci sono {current_room_objects_number} oggetti")
            for item_index, item in enumerate(current_room.items):
                print(item_index+1, '-', item)
            item_index = int(input("Quale vuoi raccogliere? "))-1
            # se l'utente usa un valore non valido
            if item_index in range(0, current_room_objects_number):
                item = current_room.items[item_index]
                player.pick_up_item(item)
                current_room.items.remove(item)
        else:
            print("La fortuna non sembra essere dalla tua parte! ")

    elif scelta == "4":
        at_least_one = False
        print("-"*40)
        for index, item in enumerate(player.inventory):
            if type(item) is Weapon:
                at_least_one = True
                print(index+1, '-', item)
        if at_least_one:
            weapon_index = int(input("Quale arma vuoi equipaggiare? "))-1
            if weapon_index in range(0, len(player.inventory)) and type(player.inventory[weapon_index]) is Weapon:
                player.equip_weapon(player.inventory[weapon_index])
        else:
            print("Non hai pozioni...")
        print("-"*40)

    elif scelta == "5":
        at_least_one = False
        print("-"*40)
        for index, item in enumerate(player.inventory):
            if type(item) is Potion:
                at_least_one = True
                print(index+1, '-', item)
        if at_least_one:
            potion_index = int(input("Quale pozione vuoi usare? "))-1
            if potion_index in range(0, len(player.inventory)) and type(player.inventory[potion_index]) is Potion:
                player.use_potion(player.inventory[potion_index])
        else:
            print("Non hai pozioni...")
        print("-"*40)

    else:
        print("ERROR")
        break