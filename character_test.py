from character import Character, Enemy

harry = Enemy( "Harry" ,"A smelly Wumpus")

harry.describe()

harry.set_conversation("Come closer. I can't see you!")

harry.talk()

harry.set_weakness("spaghetti")

print("What will you fight with?")
fight_with = input()
harry.fight(fight_with)