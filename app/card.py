from typing import List
from typing import Optional
from typing import Text

class CardType:
	def __init__(self, num=None, special=None):
		self.num = num
		self.special = special
		assert self.num or self.special

	def number_value(self) -> Optional[int]:
		# The number value of this card.
		# Returns None if the card has no number value.
		return self.num

	def special_value(self) -> Optional[Text]:
		# The special value of this card.
		# Returns None if the card is a number card.
		# Value will be one of: "peek", "draw_two", "swap"
		return self.special


def sorted_deck_factory() -> List[CardType]:
	""" Create a deck of cards per game rules. """
	_cards = []
	for _ in range(4):
		for n in range (1,10):
			_cards.append(CardType(num=n))

	for _ in range(4):
		_cards.append(CardType(special='peek'))
		_cards.append(CardType(special='draw_two'))
		_cards.append(CardType(special='swap'))

	return _cards

