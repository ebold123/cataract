from cataract.app.card import CardType
from cataract.app.card import deck_factory

class TestCard:
	def test_deck_factory():
		deck = deck_factory()

		assert ['peek']*4 == [c.special_value() for c in deck if c.special_value() == 'peek']
		assert ['draw_two']*4 == [c.special_value() for c in deck if c.special_value() == 'draw_two']
		assert ['swap']*4 == [c.special_value() for c in deck if c.special_value() == 'swap']

		for i in range(1, 10):
			assert 10 == len(c for c in deck if c.number_value() == i)