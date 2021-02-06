import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        
        self.ace_spades = Card("spades", 1)
        self.three_clubs = Card("clubs", 3)
        self.nine_hearts = Card("hearts", 9)

        self.cards = [
            self.ace_spades,
            self.three_clubs,
            self.nine_hearts
        ]

        self.card_game = CardGame()

    def test_check_for_ace(self):
        
        self.assertEqual(True, self.card_game.check_for_ace(self.ace_spades))
        self.assertEqual(False, self.card_game.check_for_ace(self.three_clubs))

    
    def test_highest_card(self):

        self.assertEqual(self.nine_hearts, self.card_game.highest_card(self.three_clubs, self.nine_hearts))
        self.assertEqual(self.nine_hearts, self.card_game.highest_card(self.nine_hearts, self.three_clubs))

    
    def test_cards_total(self):
        self.assertEqual("You have a total of 13", self.card_game.cards_total(self.cards))