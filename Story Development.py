# This is a casual route story:
# Chapter 1 project Dev:

# TODO: Change player inventory to a dictionary with weapon classes and item classes.
# TODO: Review the code to include player inventory dictionary.

# This is the player class that has all the attributes and definitions of the player:
import player
# Import the passiveDamage class module which contains all the passive damages to the player character.
import passiveDamage
# Import the available options for chapter 1.
import Options1
# Import all the cqcWeapons of chapter 1.
import cqcWeapons
# Import all ranged Weapons of chapter 1.
import rangedWeapons
# Import all defensive Items of chapter 1.
import defensiveItems
# Import all magic types of chapter 1.
import magic
# Import the value of items in chapter 1.
import itemValues

# This is where the user inputs their data to be saved onto lists and dictionaries.
input_gender = input("Enter your gender: ")
input_fname = input("Enter your first name: ")
input_lname = input("Enter your last name: ")
occupation_list = ['aristocrat', '']
gender = []
player_name = input_fname
player_lname = input_lname

#This contains the player name and gender along with the inventory and status.
player_0 = [gender, player_name]
player_inventory = []
player_useable_inventory = []
player_status = {}
gender.append(input_gender)

# These are the player options throughout chapter 1:
# Each option is different according to the story and what the player chooses.

#This the the player class which contains the player health and number statistics.

# A short list of the CQC weapons that i've listed in chapter one.
CQC_Weapons = ['longsword', 'mace', 'shortsword', 'dagger', 'punches', 'kicks', 'kitchenknife', 'treebranch', 'pan',
               'stick', 'rock', 'staff', 'random',]

# A short list of the ranged weapons that i've listed in chapter one.
ranged_weapons = ['longbow', 'shortbow', 'crossbow', 'thrownrock', 'musket',]

print("\n___Introduction___")
print(f"\nYour name is {player_name.title()}, and your gender is {gender}. You will begin your journey"
      f"in this new world. \nPlease make careful choices as it will affect the course of the story.")

print("\n\n___Chapter 1: Awakening___\nYou wake up inside of a tomb. You wake up confused not knowing what is going on."
      "\nYou get out of your coffin only to see a wooden door at the end of the room.")

# This is the first part of the story which entails waking up and getting out of the tomb.
tomb_event = True
# Choices here involve user input and if statements to distinguish user input.
while tomb_event:
    tomb_door = input("Do you open it? (yes/no) ")
    if tomb_door == 'yes':
        print(f"{player_name.title()} opens the wooden door and is introduced to the sunlight of the outside world.")
        break
    elif tomb_door == 'no':
        print(f"{player_name.title()} chose not to open the wooden door and stood still confused.")
        print(f"{player_name.title()} realizes that they need to open the wooden door.")
        continue
    else:
        print("Outside forces are working against you. Make the right decision.")
        print(tomb_door)


print("You walk outside to be greeted by a lush forest brimming with life. You hear the birds chirping and the "
      "radiant sunlight is warm. You look just ahead a find a pathway.")

# outside tomb decision making.
# something is not working here.
outside_tomb = True
while outside_tomb:
    print(options_chapter_1['options_0'])
    out_tomb = input(f"Now that you're outside of that tomb; what do you do?\n(A/B/C/D) ")
    if out_tomb.lower() == "a" or out_tomb.upper() == "A":
            print(f"\nYou walk down the pathway without a care in the world as you just woke up from a tomb. "
                  f"\n You're chilling but your lack of care has alerted a wild boar on the overgrown path.")
            after_choiceA = input(f"\nDo you chose to fight? (yes/no) ")
            if after_choiceA == "yes":
                print(f"You lunge at the boar at a sprinting speed. The boar gets scared at your sudden aggression and"
                      f" runs away.")
                print("--The Boar Fled--")
                break
            elif after_choiceA == "no":
                print(f"You decided to sneak around the boar. Your sneak skill isn't high enough to completely"
                      f" evade the boar, but the rustling of the bushes spooked the boar.")
                print("--The Boar Fled--")
                break
            else:
                print("Outside forces are working against you. Make the right decision.")
                continue
    elif out_tomb.lower() == "b" or out_tomb.upper() == "B":
            print(f"\nYou're super chilling. You look at the trees and sky outside and get distracted by a bird. "
                  f"\n Life is great.")
            after_choiceB = input("Do you want to look around or take the path? (A/C)")
            if after_choiceB.lower == "a" or after_choiceB.upper() == "A":
                print(f"You look around the tomb for a good while. You managed to find and pickup a rusty shortsword"
                      f"\n hidden away in the overgrown grass.")
                player_inventory.append('shortsword')
                print(f"Your Inventory: {player_inventory}")
            elif after_choiceB.lower == "c" or after_choiceB.upper() == "C":
                print(
                    f"You take the pathway carefully and you managed to spot a wild boar in the middle of the road grazing."
                    f"\n It seems to be relatively strong.")
                bboar_fight = input(f"Do you want to fight the boar? (yes/no) ")
                if bboar_fight == 'yes':
                    print(f"You lunge at the boar at a sprinting speed. The boar gets scared at your sudden aggression and"
                          f" runs away.")
                    print("--The Boar Fled--")
                    break
                elif bboar_fight == 'no':
                    print(f"You decided to sneak around the boar. Your sneak skill isn't high enough to completely"
                          f" evade the boar, but the rustling of the bushes spooked the boar.")
                    print("--The Boar Fled--")
                    break
                else:
                    print("Outside forces are working against you. Make the right decision.")
                    continue
            else:
                print("Outside forces are working against you. Make the right decision.")
                continue
    elif out_tomb.lower() == "c" or out_tomb.upper() == "C":
            print(f"\nYou look around the tomb for a good while. You managed to find and pickup a rusty shortsword"
                  f"\n hidden away in the overgrown grass.")
            player_inventory.append('shortsword')
            print(f"Your Inventory: {player_inventory}")
            after_choiceC = input(f"There is nothing to do here now. Will you leave the tomb area? (yes/no) ")
            if after_choiceC == "yes":
                print(f"You take the pathway carefully and you managed to spot a wild boar in the middle of "
                      f"the road grazing.\n It seems to be relatively strong.")
                cfight_boar = input(f"Do you want to fight the boar? (yes/no) ")
                if cfight_boar == "yes":
                    print("You wield your rusty shortsword and lunge straight at the boar catching it off guard. "
                          "\nYour shortsword manages to pierce to skull of the boar.")
                    print(f"--Player {player_name.title()} has recieved 35 exp. (experience points)--")
                    print(f"--Player {player_name.title()} has gained 2x boar hide.--")
                    player_inventory.append("2x boar hide")
                    player_status['level'] = 1
                    player_status['experience'] = 35
                    print(player_status)
                    print(f"Your inventory: {player_inventory}")
                    break
                elif cfight_boar == "no":
                    print(f"You decided to sneak around the boar. Your sneak skill isn't high enough to completely"
                          f" evade the boar, but the rustling of the bushes spooked the boar.")
                    print("--The Boar Fled--")
                    break
                else:
                    print("Outside forces are working against you. Make the right decision.")
                    continue
            elif after_choiceC == "no":
                print("You decide to hang around a little more. There is nothing to do so you decide to go down the"
                      " overgrown path.")
                print(f"You take the pathway carefully and you managed to spot a wild boar in the middle of "
                      f"the road grazing.\n It seems to be relatively strong.")
                cfight_boar = input(f"Do you want to fight the boar? (yes/no) ")
                if cfight_boar == "yes":
                    print("You wield your rusty shortsword and lunge straight at the boar catching it off guard. "
                          "\nYour shortsword manages to pierce to skull of the boar.")
                    print(f"--Player {player_name.title()} has recieved 35 exp. (experience points)--")
                    print(f"--Player {player_name.title()} has gained 2x boar hide.--")
                    player_inventory.append("2x boar hide")
                    player_status['level'] = 1
                    player_status['experience'] = 35
                    print(player_status)
                    print(f"Your inventory: {player_inventory}")
                    break
                elif cfight_boar == "no":
                    print(f"You decided to sneak around the boar. Your sneak skill isn't high enough to completely"
                          f" evade the boar, but the rustling of the bushes spooked the boar.")
                    print("--The Boar Fled--")
                    break
                else:
                    print("Outside forces are working against you. Make the right decision.")
                    continue
    elif out_tomb.lower() == "d" or out_tomb.upper() == "D":
            print(f"\nYou take the pathway carefully and you managed to spot a wild boar in the middle of the road grazing."
                  f"\n It seems to be relatively strong.")
            after_choiceD = input(f"Do you want to fight the boar? (yes/no) ")
            if after_choiceD == "yes":
                print(f"You lunge at the boar at a sprinting speed. The boar gets scared at your sudden aggression and"
                      f" runs away.")
                print("--The Boar Fled--")
                break
            elif after_choiceD == "no":
                print(f"You decided to sneak around the boar. Your sneak skill isn't high enough to completely"
                      f" evade the boar, but the rustling of the bushes spooked the boar.")
                print("--The Boar Fled--")
                break
            else:
                print("Outside forces are working against you. Make the right decision.")
                continue
    else:
            print("\nOutside forces are working against you. Make the right decision.")
            continue

print("\nYou continue down the overgrown path that is hidden away by dense brush. "
      "\nYou tear through the dense brush to be introduced to a well maintained road paved in brick.")
print("\nYou are given the choice to get left or right.")

while True:
    tomb_street = input('\nLeft or Right? (L/R) ')
    if tomb_street.lower() == "l" or tomb_street.upper() == "L":
        print(f"\nYou have chosen to go left. You continue to walk down the well paved path. After about an hour of "
              f"walking a city comes into view. You decide it would be optimal to visit the city.")
        break
    elif tomb_street.lower() == "r" or tomb_street.upper() == "R":
        print(f"\nYou have chosen to go right. You continue to walk down the well paved path. Nothing has come even"
              f" after three hours of walking. You see a wagon with a woman and her daughter up front.")
        wagon_0 = input(f"Do you confront the people? (yes/no)")
        if wagon_0 == 'yes':
            print(f"You confront the wagon with the woman and daughter. The woman stops the wagon visibly anxious"
                  f" at your sudden appearance. \nShe reaches inside the wagon and brings out a blade.")
            print(options_chapter_1["options_1"])
            wagon_yes = input(f"What do you say in response to this? (A/B/C/D)")
            if wagon_yes.lower() == "a" or wagon_yes.upper() == "A":
                print("\nThe woman in the wagon is very skeptical of you, but allows you to "
                      "sit on the back end of the wagon away from here and your family.")
                print("\nAfter about an hour of riding with the wagon a city comes into view."
                      " You decide it would be optimal to visit the city.")
                break
            elif wagon_yes.lower() == "b" or wagon_yes.upper() == "B":
                print("\nThe woman and the daughter next to her great weirded out by your sudden prostration "
                      "The woman then allows you to sit in the back of the wagon. ")
                print("\nAfter about an hour of riding with the wagon a city comes into view."
                      " You decide it would be optimal to visit the city.")
                break
            elif wagon_yes.lower() == "c" or wagon_yes.upper() == "C":
                print("\nThe woman listens to your explanation but doesn't understand a thing because you sound "
                      "like a psychopath. She tells you there is a city the opposite way and you should be able"
                      " to get there within 4 hours of walking. ")
                print("\nYou decide to follow her advice and walk in the opposite direction.")
                break
            elif wagon_yes.lower() == "d" or wagon_yes.upper() == "D":
                print("\nThe daughter witness you being a psychopath and are stunned. After a while they didn't"
                      " care as they gained some distance from you.")
                print("\n You reach the city in the opposite end of the road, but you're exhausted.")
                break
            else:
                print("\nOutside forces are working against you. Make the right decision.")
                continue

print(f"\nYou enter the city with other traders and wanders in front of the city.")
print(f"\n\n--Welcome to Beyruth City!--")

print(f"\n\nPresently the available facilities in the city is the --Blacksmith--, "
      f"\nthe --General Goods Store--, "
      f"\nthe --Guild House--, and"
      f"--The Inn--")

general_store_products = {}
blacksmith_products = ['']
guild_hall = ['adventure license']
the_inn = {
    'food': [''],
    'services': ['']
}

Beyruth_active = True
while Beyruth_active:
    print(options_chapter_1["options_2"])
    beyruth_choice_1 = input(f"Where would you like to go? (A/B/C/D) ")
    if beyruth_choice_1.lower() == "a" or beyruth_choice_1.upper() == "A":
        print("You have chosen to go to the blacksmith.")
        print("The blacksmith has many types of weapons but none that you can afford at the moment."
              " \nWould you like to talk to the person tending to the cashier? ")
        after_beyrught_a = input("(yes/no)")
        if after_beyrught_a == "yes":
            print("")
        elif after_beyrught_a == "no":
            print("You have decided it was not the time to talk to the cashier just yet. You walk outside the door,"
                  " and head to the nearest central square in the town.")
            continue
        else:
            print("It seems like you didn't put in the correct input. Please try again. ")
            continue
    elif beyruth_choice_1.lower() == "b" or beyruth_choice_1.upper() == "B":
        print("You have chosen to go to the General Goods Store.")
        print("The General Goods Store has a great amount of items. You are able to buy things here, "
              "as well as sell things that are currently in your inventory. "
              "\nWould you like to take a look around? (yes/no)")
        after_beyrught_b = input("(yes/no) ")
        if after_beyrught_b == 'yes':
            print("You have decided to take a look around.")
            print(f"The General Store: ", general_store_products)
            print("Would you like sell or buy? ")
            gen_store_opt = input("(buy/sell) ")
            if gen_store_opt == "buy":
                print("")
            elif gen_store_opt == "sell":
                print("What would you like to sell?")
                print(player_inventory)
                sell_0 = input("You're selling: ")
                player_inventory.pop(sell_0)
                player_inventory.append('5 coins')

        elif after_beyrught_b == "no":
            print("You have decided it was not the time to look around the store just yet. You walk outside the door,"
                  " and head to the nearest central square in the town.")
            continue
        else:
            print("It seems like you didn't put in the correct input. Please try again. ")
            continue

    elif beyruth_choice_1.lower() == "c" or beyruth_choice_1.upper() == "C":
        print("You have chosen to go to the Guild House.")
        print("At the Guild House you are able to register yourself as an adventurer and "
              "get an adventuring license."
              "\nWould you like to talk to the front desk? (yes/no)")
    elif beyruth_choice_1.lower() == "d" or beyruth_choice_1.upper() == "D":
        print("You have chosen to go to The Inn")
        print("The Inn has a bar like tavern on the first floor where food and alcohol can be served."
              " You see a woman at the front desk registering other people. "
              "\nWould you like to talk to the woman at the front desk? (yes/no")
    else:
        print(f"There are outside forces working against you. Make the right decision.")
        continue



