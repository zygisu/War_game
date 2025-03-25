class Suit:

    symbols = {"clubs":"♣", "diamonds":"♦", "hearts":"♥", "spades":"♠"} #dict. with keys and symbols

    def __init__(self, description): #creates a object with description and symbols 
        self._description = description
        self._symbol = Suit.symbols[description.lower()] #Suit. - name of class. symbols key of description 

    @property #getters becouse those cant be modified outside the class 
    def description(self):
        return self._description #_means that it can be used only inside tha class
    
    @property
    def symbol(self):
        return self._symbol

class Card:

    special_cards = {11: "Jack", 12: "Queen", 13: "King", 14:"Ace"}

    def __init__(self, suit, value): #if those values wanted to be used outside of class, getters should be used as below. 
        self._suit = suit
        self._value = value

    @property 
    def suit(self):
        return self._suit
    
    @property
    def value(self):
        return self._value
    
    def show(self):
        card_value = self._value
        card_suit = self._suit._description.capitalize()
        suit_symbol = self._suit.symbol

        if self.is_special():
            card_description = Card.special_cards[card_value]
            print(f"{card_description} of {card_suit} {suit_symbol}")
        else:
            print(f"{card_value} of {card_suit} {suit_symbol}")

    def is_special(self):
        return self._value >= 11
