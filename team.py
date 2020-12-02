# TODO Create an empty list to maintain the player names
PlayerNames = []
UserChoice = "y"
i = 1

while UserChoice.lower() == "y":
    UserChoice = input("Would you like to add players to the list? (y/N): ")
    if UserChoice.lower() == "y":
        NewPlayerName = input("What's the name of the player you wish to add?: ")
        PlayerNames.append(NewPlayerName)

print("There are {} players on the team".format(len(PlayerNames)))
for player in PlayerNames:
    print(i, player)
    i += 1
    
GKNr = input("Please select a goal keeper using a number from the list: ")
print("The goalkeeper's name is", PlayerNames[int(GKNr)-1])          
##print(int(GKNr)-1)    
# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'


# TODO print the number of players on the team
  

# TODO Print the player number and the player name
# The player number should start at the number one


# TODO Select a goalkeeper from the above roster


# TODO Print the goal keeper's name
# Remember that lists use a zero based index

