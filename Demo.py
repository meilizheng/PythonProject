## Import the Player class from the Player
from Player import Player;
# Global collection of Players
players = [
    Player("Alex", 10),
    Player("Olivia", 13),
    Player("Ethan", 24),
    Player("Sophia", 15),
    Player("Jackson", 18)
]

#def in Python is used to define a function
#define a display_all_players function
def display_all_players():
    """Display all players' names and numbers."""
    print("All Players:")
    # for loop in Pyton
    for player in players:
        #out put player's name and player'number
        print(f"{player.name} - Number: {player.number}")

#define a display_players_with_odd_numbers function
def display_players_with_odd_numbers():
    """Display players with odd numbers."""
    print("Players with Odd Numbers:")
    #for loop
    for player in players:
        #use if to check if the player's number is a odd number or not
        if player.number % 2 != 0:
            #if is odd, display the player's name and number
            print(f"{player.name} - Number: {player.number}")

#define a display_players_with_starting_letter function
def display_players_with_starting_letter(letter):
    """Display players with names starting with the given letter."""
    print(f"Players with Names Starting with '{letter}':")
    # Flag to check if at least one player is found
    found_players = False

    # Use a for loop to check each player's name with the specific letter that the user entered
    for player in players:
        # If the player's name starts with the letter that the user entered, display the player
        if player.name.startswith(letter.upper()):
            print(f"{player.name} - Number: {player.number}")
            found_players = True
            #use break to exit the for loop
            break
    # Check if no players were found
    if not found_players:
        #in Python 'f' lick '$' in c#
        print(f"No players found with the {letter} letter.")

#define a add_plyer function
def add_player():   
    """Add a new player to the list."""
    #let user add new player
    name = input("Enter player name: ")
    #use the casting to cast number
    number = int(input("Enter player number: "))
    #create a new instance and assign value
    new_player = Player(name, number)
    #use append add new player to the player list
    players.append(new_player)
    print(f"Player {name} added successfully.")

# Main menu
while True:
    print("\nMenu:")
    print("1. Display all players")
    print("2. Display players with odd numbers")
    print("3. Display players with names starting with a letter")
    print("4. Add a new player")
    print("5. Quit")
    
    #let use choose a fuction
    choice = input("Enter your choice (1-5): ")
    #use if elif to check whick fuction user choose.
    if choice == "1":
        display_all_players()
    elif choice == "2":
        display_players_with_odd_numbers()
    elif choice == "3":
        letter = input("Enter a letter: ")
        display_players_with_starting_letter(letter)
    elif choice == "4":
        add_player()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
