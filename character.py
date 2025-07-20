class Character:
    def __init__(self, char_name, char_description):
        self.char_name = char_name
        self.char_description = char_description
        self.conversation = None
    
    def describe(self):
        print( self.char_name  + " is here")
        print(self.char_description)
    
    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation:
            print("[" + self.char_name + " says]: " + self.conversation)
        else:
            print(self.char_name + " does not want to talk to you")
        
    def fight(self, combat_item):
        print(self.char_name + " does not want to fight you")
        return True
    

class Enemy(Character):
    enemies_to_defeat = 3
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1    

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You defeated " + self.char_name + " and successfully captured him with " + combat_item + "!")
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            return True
        else:
            print("You have been outsmarted by " + self.char_name + " and have been defeated!")
            return False


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def hi_five(self):
        print(self.char_name + " high fives you back!")