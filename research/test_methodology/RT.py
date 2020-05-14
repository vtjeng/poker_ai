from typing import Dict

from RT_cfr import *
from pluribus.games.short_deck.state import *
from pluribus.poker.card import Card


if __name__ == "__main__":
    utils.random.seed(38)
    public_cards = [Card("ace", "spades"), Card("queen", "spades"), Card("queen", "hearts")]
    # we load a (trained) strategy
    agent1 = TrainedAgent("../blueprint_algo/results_2020_05_10_21_36_47_291425")
    action_sequence = ["raise", "call", "raise", "call", "call", "call"]
    agent_output = train(agent1.offline_strategy, public_cards, action_sequence, 150, 20, 20, 3, 1, 50) # TODO: back to 50
    import ipdb;
    ipdb.set_trace()
