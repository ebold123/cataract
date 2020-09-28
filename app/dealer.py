from typing import List
from typing import Optional
from typing import Text

import click
import itertools
import random

from player import PlayerBase
from dumb_player import DumbPlayer
from card import sorted_deck_factory
from card import CardType

def get_player_map() -> Dict[Text, classobj]:
	return {DumbPlayer.name: DumbPlayer}

def player_factory(num_players: int, player_styles: List[classobj]) -> List[PlayerStyleBase]:
	use_styles = itertools.cycle(player_styles)
	return [player_class() for player_class in use_styles]

@click.command()
@click.option('-n', '--num_players', type=int, default=4)
@click.option('-s', '--player_style', type=Text, multiple=True)
def main(num_players, player_style):

	# Init
	player_style = [DumbPlayer]
	current_players = player_factory(num_players, player_style)
	assert current_players
	assert len(current_players) > 1

	deck = sorted_deck_factory()
	random.shuffle(deck)
	print(', '.join([d for d in deck]))
	# discard_pile = [] # type: List[CardType]

	# Deal hands



	# Loop through players until rat-a-tat-cat

	# Tally scores and determine wwinner


if __name__ == '__main__':
	main()