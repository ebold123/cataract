from actions import PlayerAction
from card import CardType
from typing import List

class PlayerBase:
	"""
	You should create a subclass of this abstract-ish base class.
	You should implement play_hand.
	You may persist data between hands in player_memory; for instance
	any cards you've peeked of other players.
	"""
	def __init__(self):
		self.player_memory = {'example': [1, 2, 10000]}


	def play_hand(
		self,
		top_deck_card:CardType, 
		your_visible_cards:List[CardType]) -> PlayerAction:

		pass