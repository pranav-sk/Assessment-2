from room import Room
from character import Character, Enemy

platform = Room("Platform")
platform.set_description("A long and wide train platform used by the mafia to run their illegal industry. On the left, covering 50% of the platform is the Loading zone with a storage. To the right is the Passenger Zone of the platform. In front of you are the platform screen doors, which form a barrier between the passengers and the tracks. Behind you is the lift you used to come here.")
loading = Room("Loading Zone")
loading.set_description("The left hand side of the platform, which is used to load all the goods from the Goods Storage into the train. Behind you in the left corner of the platform is the Goods Storage where they store all their illicit goods. To the right is the Passenger Zone of the platform.")
goods_storage = Room("Goods storage")
goods_storage.set_description("A big room used to store all the illegal goods for Big Tony's mafia business. Located in the back left corner of the Loading Zone, They take the goods from here and load them into the train.")
basement = Room("Basement")
basement.set_description("The basement of the police station is one level below the ground level. It is also where the police cars park.")
ground = Room("Ground level")
ground.set_description("The ground level of the police station is where the main entrance is located.")
jail_cell = Room("Jail Cell")
jail_cell.set_description("A small room with a bed and a toilet. It is where the prisoners are kept. The cell is located on the ground level of the police station.")
level1 = Room("Level 1")
level1.set_description("Located above the ground level, a lobby with a presentation room over towards the right-hand side of the room.")
presentation_room = Room("Presentation Room")
presentation_room.set_description("A room where all meetings are held.")
level2 = Room("Level 2")
level2.set_description("Located above level 1, this is also where the case file rooms are located.")
UC_offices = Room("Undercover Cops' Offices")
UC_offices.set_description("This is your office, you have a desk with all your files and resources.")
filing_room = Room("Case Files Rooms")
filing_room.set_description("A room filled with evidence. Files, warrents and more.")

platform.link_room(loading, "right")
loading.link_room(platform, "left")
loading.link_room(goods_storage, "right")
goods_storage.link_room(loading, "left")
platform.link_room(basement, "up")
basement.link_room(platform, "down")
basement.link_room(ground, "up")
ground.link_room(basement, "down")
ground.link_room(jail_cell, "left")
jail_cell.link_room(ground, "right")
ground.link_room(level1, "up")
level1.link_room(ground, "down")
level1.link_room(presentation_room, "right")
presentation_room.link_room(level1, "left")
level1.link_room(level2, "up")
level2.link_room(level1, "down")
level2.link_room(UC_offices, "right")
UC_offices.link_room(level2, "left")
level2.link_room(filing_room, "left")
filing_room.link_room(level2, "right")

big_Tony = Enemy("Big Tony", "The grand Mafia boss of Sydney, and NSW's most wanted criminal")
big_Tony.set_conversation(f"Well, well, well ... if it isn't the police. I see you have finallyfound my secret underground railway system. Took you long enough.")
big_Tony.set_weakness("spaghetti")
goods_storage.set_character(big_Tony)



# Start the game
print("Welcome to the Undercover Cops Game!")

current_room = UC_offices
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")


current_room = loading
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")


current_room = goods_storage
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character(big_Tony)
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = basement
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = ground
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = jail_cell
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = level1
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = presentation_room
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = level2
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = platform
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = filing_room
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go or do, Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Congratualtions, you have successfully won the fight and captured Big Tony!")
                current_room.set_character(None)
            else:
                print("Give up, you have been outsmarted and lost the fight.")
                print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dead = True
        else:
            print("There is no one here to fight with")






