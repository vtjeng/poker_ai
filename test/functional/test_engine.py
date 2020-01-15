import pytest


@pytest.mark.parametrize("n_players", [2, 4, 6])
def test_hand(n_players):
    """Test a hand can be played."""
    from pluribus.game.table import PokerTable
    from pluribus.game.engine import PokerEngine
    from pluribus.game.player import Player
    from pluribus.game.pot import Pot
    initial_chips_amount = 10000
    small_blind_amount = 10
    big_blind_amount = 50
    pot = Pot()
    players = [
        Player(
            name=f'player {player_i}',
            initial_chips=initial_chips_amount,
            pot=pot)
        for player_i in range(n_players)
    ]
    table = PokerTable(players=players, pot=pot)
    engine = PokerEngine(
        table=table,
        small_blind=small_blind_amount,
        big_blind=big_blind_amount)
    engine.play_one_round()
