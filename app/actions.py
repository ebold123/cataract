from typing import Optional
from typing import Text

PLAYER_ACTIONS = ['draw_two', 'peek', 'swap']

class PlayerAction:
	def __init__(self, action:Text, other_player:Optional[int], my_card_id:Optional[int], other_card_id:Optional[int]):

		if action not in PLAYER_ACTIONS:
			raise ValueError('Invalid action')

		self.action = action
		self.my_card_id = my_card_id
		self.other_card_id = other_card_id

		if self.action == 'draw_two' and (self.other_player or self.other_card_id or self.my_card_id):
			raise ValueError('draw_two requires no other arguments')
		if self.action == 'peek' and (not self.other_player or not self.other_card or self.my_card):
			raise ValueError('peek requires only other_player and other_card_id')
		if self.action == 'swap':
			if not self.other_player or not self.other_card or not self.my_card:
			raise ValueError('swap requires other_player and my_card_id and other_card_id')


