import pytest
from viper import compiler
from ethereum.tools import tester as t

TEN_MINUTES = 600

# To be moved to test_dice.py
@pytest.fixture
def dice():
    tester = t
    dice_c = open('contracts/cryptodice.v.py')
    dice = dice_c.read()
    dice_c.close()
    tester.s = t.Chain()
    tester.s.head_state.gas_limit = 10**9
    tester.playerA = (t.a0, t.k0)
    tester.c = tester.s.contract(
        dice,
        language='viper',
        args=[tester.playerA[0], 100, TEN_MINUTES]
    )
    return tester

# To be moved to test_coinflip.py
@pytest.fixture
def coin():
    tester = t
    coin_c = open('contracts/cryptoflip.v.py')
    coin = coin_c.read()
    coin_c.close()
    tester.s = t.Chain()
    tester.s.head_state.gas_limit = 10**9
    tester.playerA = (t.a0, t.k0)
    tester.c = tester.s.contract(
        coin,
        language='viper',
        args=[tester.playerA[0], 100, TEN_MINUTES]
    )
    return tester

# To be moved to conftest
@pytest.fixture
def assert_tx_failed(t):
    def assert_tx_failed(function_to_test, exception = t.TransactionFailed):
        initial_state = t.s.snapshot()
        with pytest.raises(exception):
            function_to_test()
        t.s.revert(initial_state)
    return assert_tx_failed

# To be moved to conftest
@pytest.fixture
def get_logs():
    def get_logs(receipt, contract, event_name=None):
        contract_log_ids = contract.translator.event_data.keys()
        logs = [log for log in receipt.logs \
                if log.topics[0] in contract_log_ids and \
                log.address == contract.address and \
                (not event_name or \
                 contract.translator.event_data[log.topics[0]]['name'] == event_name)]
        assert len(logs) > 0, "No logs in last receipt"
        return [contract.translator.decode_event(log.topics, log.data) for log in logs]
    return get_logs

def pad_bytes32(instr):
    """ Pad a string \x00 bytes to return correct bytes32 representation. """
    bstr = instr.encode()
    return bstr + (32 - len(bstr)) * b'\x00'

# To be moved to test_dice.py
def test_cryptodice_log(dice, get_logs):
    #tester.c.request(QUERY, sender=t.k1, value=50)
    #receipt = tester.s.head_state.receipts[-1]
    #logs = get_logs(receipt, tester.c)
    #assert len(logs) == 1
    #assert logs[0]["_event_type"] == b'Request'
    #assert logs[0]["_sender"] == '0x' + t.a1.hex()
    #assert logs[0]["_query"] == pad_bytes32(QUERY)
    pass
