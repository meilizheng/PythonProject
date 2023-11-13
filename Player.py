#declares a class named Player
class Player:
    #Constructor
    # In Python 'self' like 'this' in C# when you create a constructor
    #name and number are two pramater that will be passed when creating an instance in main. they represent the player's name and player'number
    def __init__(self, name, number):
        self.name = name
        self.number = number