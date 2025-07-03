class Character:
    def __init__(self, char_name, char_description):
        self.char_name = char_name
        self.char_description = char_description
        self.conversation = None
    
    def describe(self):
        print("Officer" +  self.char_name  + "is here!")
        print(self.char_description)
    
    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation:
            print("[" + self.char_name + " says]: " + self.conversation)
        else:
            print(self.char_name + " does not want to you")
        
    def fight(self, combat_item):
        print(self.char_name + " does not want to fight you")
        return True