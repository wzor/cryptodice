import pytest
from viper import compiler
from ethereum.tools import tester as t

@pytest.fixture
def random_t():
    tester = t
    random_c = open('contracts/random.v.py')
    random = random_c.read()
    random_c.close()
    tester.s = t.Chain()
    tester.s.head_state.gas_limit = 10**9
    tester.c = tester.s.contract(
        random,
        language='viper'
    )
    return tester
