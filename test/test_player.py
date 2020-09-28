from cataract.app.actions import Action
from cataract.app.card import CardType
from cataract.app.player import PlayerBase


class PlayerSubclass(PlayerBase):
	pass

class TestPlayerBase:
	def setup(self):
		self.player = PlayerSubclass()

	def test_player(self):
		mock_card = CardType(num=5)

		self.player.play_hand(top_deck_card=mock_card)
