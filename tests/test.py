import pytest
import ethereum.utils as utils

TEN_MINUTES = 600

@pytest.fixture
def coinflip_tester(t):
    from viper import compiler
    t.languages['viper'] = compiler.Compiler()
    contract_code = open('contracts/coinflip.v.py').read()
    t.c = t.s.contract(contract_code, language='viper', args=[t.accounts[0], 1000, TEN_MINUTES])
    return t

def test_initial_state(coinflip_tester):
    # Check seller is correct
    assert utils.remove_0x_head(coinflip_tester.c.get_seller()) == coinflip_tester.accounts[0].hex()
    # Check waiting time is ten minutes
    assert coinflip_tester.c.get_bet_end() == coinflip_tester.s.head_state.timestamp + 600
