import numpy as np
import yaml
import IPython
from itertools import zip_longest

cities = [
    "New York",
    "Washington",
    "London",
    "Istanbul",
    "Tripoli",
    "Cairo",
    "Lagos",
    "Sao Paolo",
    "Jacksonville",
]

starting_deck = [city for city in cities for _ in range(3)]

city_colors = {
    "New York": "blue",
    "Washington": "blue",
    "London": "blue",
    "Istanbul": "black",
    "Tripoli": "black",
    "Cairo": "black",
    "Lagos": "yellow",
    "Sao Paolo": "yellow",
    "Jacksonville": "yellow",
}

infection_deck = []
discard_pile = []
infection_cards = len(starting_deck)

def save():
    # Save the game state to a file
    # infection_deck
    # discard_pile

    yaml.dump(infection_deck, open("infection_deck.yaml", "w"))
    yaml.dump(discard_pile, open("discard_pile.yaml", "w"))

def load():
    # Load the game state from a file
    # infection_deck
    # discard_pile

    with open("infection_deck.yaml", "r") as file:
        infection_deck = yaml.safe_load(file)
    with open("discard_pile.yaml", "r") as file:
        discard_pile = yaml.safe_load(file)
    return infection_deck, discard_pile

def draw(card):
    # Convert card to title case
    card = card.title()
    
    # Record which city card is drawn
    # Move the card from the infection deck to the discard pile

    if card in infection_deck:
        infection_deck.remove(card)
        discard_pile.insert(0, card)
    else:
        print(f"Card {card} not in infection deck.")

def print_state():
    print()
    print(20 * "-")
    print("Infection deck:\t\tDiscard pile:")
    for card_infection, card_discard in zip_longest(infection_deck, discard_pile, fillvalue=''):
        print(f"{card_infection}\t\t{card_discard}")
    print(20 * "-")

def predict():
    # Print the probability of drawing each card in the infection deck
    global infection_deck, cities

    total_cards = len(infection_deck)
    if total_cards == 0:
        return
    print()
    for city in cities:
        city_cards = infection_deck.count(city)
        probability = city_cards / total_cards
        print(f"{city.ljust(15)} {str(city_cards).ljust(5)} {probability:.2f}")
    

def main_loop():
    # Ask for user input
    # acceptable inputs are:
    # save
    # load
    # draw
    # print
    # quit

    global infection_deck, discard_pile, infection_cards

    while True:
        predict()
        print()
        print(20 * "-")
        user_input = input("init, save, load, draw, print, quit, debug\n\n>>>")
        if user_input == "init":
            infection_deck = starting_deck.copy()            

        elif user_input == "save":
            save()

        elif user_input == "load":
            infection_deck, discard_pile = load()

        elif user_input == "draw":
            user_input = input("Which card was drawn?\n")
            draw(user_input)
            
        elif user_input == "print":
            print_state()
            
        elif user_input == "quit":
            break
        elif user_input == "debug":
            IPython.embed()
        else:
            print("Invalid input, please try again")

main_loop()