Start: __log__({_seller: indexed(address), _amount: wei_value})
Bid: __log__({_player: indexed(address), _amount: wei_value})
Played: __log__({_winner: indexed(address), _amount: wei_value})

bet_value: public(wei_value)
bet_start: public(timestamp)
bet_end: public(timestamp)

seller: public(address)
player: public(address)
odd: public(bool)

sold: public(bool)
ended: public(bool)

@public
def __init__(_seller: address, _bet_value: wei_value, _waiting_time: timedelta):
    self.seller = _seller
    self.bet_value = _bet_value
    self.bet_start = block.timestamp
    self.bet_end = self.bet_start + _waiting_time
    log.Start(self.seller, self.bet_value)

@public
@payable
def bid(_bet: bool):
    assert block.timestamp < self.bet_end
    assert msg.value == self.bet_value
    self.player = msg.sender
    self.odd = _bet
    self.sold = True
    log.Bid(self.player, self.bet_value)

@public
def play():
    assert block.timestamp >= self.auction_end
    assert not self.ended
    if self.sold:
        outcome = compare(self.odd)
        if outcome:
            send(self.player, self.bet_value)
            log.Played(self.player, self.bet_value)
        else:
            send(self.seller, self.bet_value)
            log.Played(self.seller, self.bet_value)
    self.ended = True

@private
def random():
    return as_num256(sha3(block.timestamp))

@private
def compare(_odd):
    result = self.random % 2
    if _odd:
        return result > 0
    else:
        return result == 0
