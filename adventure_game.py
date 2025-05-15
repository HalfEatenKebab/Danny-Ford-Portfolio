#------------------------------------------------------------------------------------------------
# Starting code which prompts user for first choice

def start():
    print("\nWelcome to this mini adventure terminal game, press enter when you are ready to start")
    enter = input("> ")
    print("\nYou have been travelling for miles and are in despearte need for water.")
    print("You approach a fork in the road, do you go left or right?")
    first_choice()


def first_choice():
    path_choice = input("> ")
    if path_choice in ["left","Left"]:
        print("You stroll into a woods and hear a stream running in the distance.")
        print("You also hear what sounds like the heavy movement of a bear.")
        go_left()
    elif path_choice in ["right", "Right"]:
        print("You approach a tavern which looks very much open. Fumbling for your bag you look to see if you have any money")
        go_right()
    else:
        print("I know your mind is weaary, but think staight, left or right?")
        del path_choice
        first_choice()


# -----------------------------------------------------------------------------------------------
# All choices after getting 'left' input

def go_left():
    print("Do you:\n 1. Pull out your sword \n 2. Approach quietly")
    sword = input("1 or 2?\n > ")
    if sword == "1":
        print("You draw out your sword and bravely move towards the heavy sounds of a bear")
        print("As you get closer to the sound of the stream, the sounds of the bear have disappeared, you sigh with relief and run towards the stream, gasping for a drink")
        print("You get to the river, do you take a drink?\n ")
        drink()
    elif sword == "2":
        print("You crouch down and move towards the stream")
        print("Quietly moving through the bushes, the sounds of the stream become louder and the sounds of the bear disappear, you let out a sigh of relief and carry on moving towards the stream slowly")
        print("\nAs you get to the river you hear a rustle in the tree, suddenly a bear jumps down wearing a monocle and a top hat.")
        tree_bear()

def drink():
    water = input("> ")
    if water in ["y", "Y", "Yes", "yes", "YES"]:
        bear()
    else:
        print("Are you sure? You are really thirsty.")
        del water
        drink()

def bear():
    print("A bear with a top hat and a monocle jumps down from the tree. Anger strikes it when it sees your sword laying next to you.")
    print(''' "How dare you come to my watering hole with such a threat at hand" The bear says.''')
    print("Before you even get chance to go for your sword, the bear swipes at you and everything goes black")

def tree_bear():
    print('''"You look very thirsty weary traveller, I have a refreshing moutain dew for such innocent person."''')
    print("Do you take the drink?")
    drink = input("> ")
    if drink in ["y", "Y", "Yes", "yes", "YES"]:
        print("You drink the refreshing moutain dew and become enlighted. \n The dignified gentleman of a bear offers you a lift on his back and you ride out of the forrest and into the sunset.")
        print("\n THE END \n")
    else: 
        print("The dignified bear is offened at your response and swipes at you for such rudeness. \n Everything goes black.")

#------------------------------------------------------------------------------------------------
# All choices from 'right' input

def go_right():
    bag = ['Sword', 'Map', 'Money']
    print("\nYou have: ")
    for item in bag:
        print(f"~ {item}")
    print("\nWhat do you you want to take out?")
    held_item = input("> ")
    if held_item in ['money','Money']:
        print(f"You pulled out the {held_item}\n")
        bag.pop(2)
        print(f"You enter the tavern and go up to the bar to order a refreshing lemonade and hand the bar maid your {held_item}")
        print("As you go to have a drink, a brute smacks the drink out of your hand and throws you across the bar.")
        print('''\n "I know where you have come from kid" the brute expresses in an angry tone. "Hand me over the map from the king and I'll spare you" ''')
        tavern_approach(bag)
    elif held_item in ['Sword','sword','Map','map']:
        print(f''' "A {held_item} won't be useful right now" you think to yourself''')
        go_right()
    else:
        print(f"You don't have {held_item}, try another look")
        go_right()

def tavern_approach(bag):
    print("You stumble into your bag looking at two options, what do you choose?\n")
    for item in bag: 
        print(f" ~ {item}")
    
    for chances in range(4):
        if chances == 3:
            print("\nThe brute becomes tired of waiting, he pulls out his sword and strikes it into your chest, as life fades from you, the last thing you see if the brute pulling the map from your bag...")
        else:
            choice = input("> ")
            if choice in ['sword', 'Sword']:
                print("\n You go to pull out your sword to engange with the brute, however with a sudden sharp pain in your back, a blade pierces through you. A hidden minion had been waiting for such a rumble to arise. You watch them steal the map from your bag and laugh as they walk out the tavern doors")
                exit()
            elif choice in ['map', 'Map']:
                print('''\nYou hand over the map trembling with fear, in hopes the brute doesnt engage with you. He laughs in your face and cries with joy "That was to easy" and walks out the door. \n You are left cautious of what to do next, you can't go home, they'll hang you by the neck''')
                exit()
            else:
                print("You haven't got time to fumble, make up your mind now!!")
        

#------------------------------------------------------------------------------------------------
start()




