class Character:
    def __init__(self, char_name, char_description):
        self.char_name = char_name
        self.char_description = char_description
        self.conversation = None
    
    def describe(self):
        print(self.char_name  + " is here!")
        print(self.char_description)
    
    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation:
            print("[" + self.char_name + " says]: " + self.conversation)
        else:
            print(self.char_name + " doesn't want to talk to you")   
        
    def fight(self, combat_item):
        print(self.char_name + " doesn't want to fight you")
        return True
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You have left " + self.char_name + " weak and heartbroken, but have successfully captured him with the " + combat_item )
            return True
        else:
            print(self.char_name + " has outsmarted you and has knocked you out, you unworthy officer")
            return False