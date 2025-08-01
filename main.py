from room import Room
from character import Character, Enemy, Friend
from item import Item

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
filing_room.set_description("A room filled with evidence. Files, warrants and more.")

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
big_Tony.set_conversation("Well, well, well ... if it isn't the undercover police. I see you have finally found my secret underground railway system. Took you long enough.")
big_Tony.set_weakness("spaghetti")
goods_storage.set_character(big_Tony)

tim = Friend("Tim", "Your best friend who is co-working with you in the undercover cops case. He is always there to help you out, and is fearless as he skillfully fights alongside you.")
tim.set_conversation("Goodday Offs, I am here to help you out with the case. There was no luck in finding Big Tony, but we found a letter that he wrote and left in the Jail cell. You should go get it, it might be a clue to finding him. I will be here in the UC_offices if you need me.")
UC_offices.set_character(tim)

# Create an item
letter_one = Item("Letter 1")
letter_one.set_description("A letter which was found in the Jail cell. It is written by Big Tony himself, and it has the word 'Clue#1'written in bold letters on the top of the letter. It is a clue to finding Big Tony.")
jail_cell.set_item(letter_one)

letter_two = Item("Letter 2")
letter_two.set_description("A letter which was found on your desk in the UC_offices. It is written by Big Tony himself, and it has the word 'Clue#2' written in bold letters on the top of the letter. This is the second clue to finding Big Tony.")
presentation_room.set_item(letter_two)

letter_three = Item("Letter 3")
letter_three.set_description("A letter which was found in the basement. It is written by Big Tony himself, and it has the word 'Clue#3' written in bold letters on the top of the letter. This is the third and final clue to finding Big Tony. ")
basement.set_item(letter_three)

arrest_warrant = Item("The Arrest Warrant")
arrest_warrant.set_description("An arrest warrant for Big Tony, issued by the police department. It is a legal document that allows you to arrest Big Tony. It has the following message: 'You are hereby ordered to arrest Big Tony, the grand Mafia boss of Sydney, and NSW's most wanted criminal.'")
filing_room.set_item(arrest_warrant)

gun_taser = Item("gun and taser")
gun_taser.set_description("Your department issued gun and taser, which you must have with you at all times. It is a standard issue gun and taser for undercover cops. Taser is used to control criminals without causing permanent harm, and the gun is used to protect yourself in case of an emergency.")
level2.set_item(gun_taser)

spaghetti = Item("spaghetti")
spaghetti.set_description("An unopened packet of spaghetti, sounds to stupid to be a weapon, but is more lethal than you think.")
UC_offices.set_item(spaghetti)

badge_cuffs = Item("badge and cuffs")
badge_cuffs.set_description("Your department issued badge and handcuffs, which you must have with you at all times. It is your only proof showing that you're a cop since you are undercover and the handcuffs are used to detain criminals.")
ground.set_item(badge_cuffs)
bag = [gun_taser, spaghetti, badge_cuffs]

# Start the game
print("Welcome to the Undercover Cops Game Simulator, Officer!")
print("You are an undercover cop who is trying to catch Big Tony, the grand Mafia boss of Sydney, and NSW's most wanted criminal.")
print("You will be exploring the police station and the underground railway system, collecting evidence and fighting enemies to catch Big Tony.")
print("Big Tony has escaped from the jail cell of the station and has gone into hiding.")
print("You will need to find clues and evidence to catch him, and you will also need to fight enemies along the way.")
print("However, you must first find and collect your gun and taser and your badge and cuffs because it is department standards.")
print("You will also need to find your friend Tim, who is co-working with you in the undercover cops case.")
print("Good luck, Officer!")



current_room = ground
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take, read or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")

    elif command == "take":
        if item is not None:
                print("You picked up " + item.get_name() + " and placed it in your bag.")
                bag.append(item.get_name())
                current_room.set_item(None)
        else:
            print("There is no item here to pick up.")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")


current_room = loading
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    
    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")

    elif command == "take":
        if item is not None:
            print("You picked up " + item.get_name() + " and placed it in your bag.")
            bag.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is no item here to pick up.") 

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = goods_storage
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")

    elif command == "take":
        if item is not None:
            print("You picked up " + item.get_name() + " and placed it in your bag.")
            bag.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is no item here to pick up.")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = basement
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take, read or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")

    elif command == "take":
        if item is not None:
            print("You picked up " + item.get_name() + " and placed it in your bag.")
            bag.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is no item here to pick up")

    elif command == "read":
        if item is not None:
            print("You read the " + item.get_name() + ":")
            print(" AHHHHHHHHHHHHHHHHH! You have found my third and final clue to finding me. Here it is: ' My secret office is not where anyone to expect it to be. Sometimes you can't think where it is. Maybe you should think what is below you.' Remember to be armed before finding me, cause I am not coming down without a fight.")
            if item.get_name() == "Letter 3":
                print("You have found the third clue to finding Big Tony!")
                print("Now you need to find your gun and taser, the arrest warrant, spaghetti and your badge and cuffs, and then you can go find Big Tony.")
        else:
            print("There is no item here to read")
           
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")
    
current_room = UC_offices
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")

    elif command == "take":
        if item is not None:
            print("You picked up " + item.get_name() + " and placed it in your bag.")
            bag.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is no item here to pick up")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = jail_cell
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take, read or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    
    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")

    elif command == "take":
        if item is not None:
            print("You picked up " + item.get_name() + " and placed it in your bag.")
            bag.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is no item here to pick up")
    
    elif command == "read":
        if item is not None:
            print("You read the " + item.get_name() + ":")
            print("Greetings, officer. I am Big Tony, the grand Mafia boss of Sydney, and NSW's most wanted criminal. I have escaped from the clutches of your justice system and am now hiding away in my secret factory. You will never catch me! But if you want to try, find the three clues I left you. Here is your first: 'I own a transporting business and use a specific mode of transport. For the second clue in the station, continue your search up and up'. Good luck finding me.")
            if item.get_name() == "Letter 1":
                print("You have found the first clue to finding Big Tony!")
                print("Now you need to find the second clue that will help you find Big Tony.")
        else:
            print("There is no item here to read")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = level1
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")
    
    elif command == "take":
        if item is not None:
            print("You picked up " + item.get_name() + " and placed it in your bag.")
            bag.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is no item here to pick up")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = presentation_room
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take, read or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")

    elif command == "take":
        if item is not None:
            print("You picked up " + item.get_name() + " and placed it in your bag.")
            bag.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is no item here to pick up")

    elif command == "read":
        if item is not None:
            print("You read the " + item.get_name() + ":")
            print("Greetings, again. Well done! I see that you have found my second clue to finding me. Here it is: 'My Nonna told me that if I was doing something illegal, do it the right way. My third clue is hidden in a room where down where you used to enter and exit when you were on patrol.' Good luck finding me.")
            if item.get_name() == "Letter 2":
                print("You have found the second clue to finding Big Tony!")
                print("Now you need to find the spaghetti and then you can go find your final clue.")
        else:
            print("There is no item here to read")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = level2
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")

    elif command == "take":
        if item is not None:
            print("You picked up " + item.get_name() + " and placed it in your bag.")
            bag.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is no item here to pick up")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = platform
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")

    elif command == "take":
        if item is not None:
            print("You picked up " + item.get_name() + " and placed it in your bag.")
            bag.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is no item here to pick up")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")

current_room = filing_room
dead = False
while dead == False:
    print("/n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    print("Where would you like to go (up, down, left or right) or do (talk, hi_five, take or fight), Officer?")
    command = input(">")
    if command in ["up", "down", "left", "right"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    
    elif command == "hi_five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(" I wouldn't high five him if I were you...")
            else:
                inhabitant.hi_five()
        else:
            print("There is no one here to high five :(")

    elif command == "take":
        if item is not None:
            print("You picked up " + item.get_name() + " and placed it in your bag.")
            bag.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is no item here to pick up")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Congratulations, you have successfully won the fight and captured Big Tony!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You have defeated all the enemies and completed the game!")
                        dead = True
                else:
                    print("You have been outsmarted by " + inhabitant.char_name + " and have been defeated!")
                    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    dead = True
            else:
                print("You don't have a " + fight_with + " to fight with.")
                dead = True
        else:
            print("There is no one here to fight with")
