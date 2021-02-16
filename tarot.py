# Tarot Reading Program

import csv
import random

with open('tarot cards.csv') as tarot_csv: # To import card descriptions and meanings from a CSV file
    
    deck = {}
    tarot_contents = csv.DictReader(tarot_csv)
    for line in tarot_contents:
        deck[line['Card']] = {
            'card number': line['Card Number'], 
            'suit': line['Suit'],
            'upright meaning': line['Upright Meaning'],
            'reversed meaning': line['Reversed Meaning'],
            'image': line['Image']
            }

class Tarot_Deck:
    def __init__(self, deck_of_cards):
        self.deck = deck_of_cards

    def draw_card(self, cards_to_draw=1):
        cards = [card for card in self.deck]
        cards_drawn = random.sample(cards, k = cards_to_draw)
        self.cards_drawn = cards_drawn
        if cards_to_draw == 1:
            print('A card has been drawn.')
        else:
            print('Cards have been drawn.')
    
    def celtic_cross(self):
        self.draw_card(12)

    def past_present_future(self):
        self.draw_card(3)

    def show_meaning(self):
        print('You have asked, and so I shall reveal. Here is your fate:')
        for card in self.cards_drawn:
            upright = random.choice([True, False])
            if upright == True:
                upright_meaning = self.deck[card].get('upright meaning')
                print('{card}: {meaning}'.format(card=card, meaning=upright_meaning))
            else:
                reversed_meaning = self.deck[card].get('reversed meaning')
                print('{card} Reversed: {meaning}'.format(card=card, meaning=reversed_meaning))

    def end_reading(self):
        self.cards_drawn = []
     
my_deck = Tarot_Deck(deck)
