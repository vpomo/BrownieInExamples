import brownie

def test_read_event(usdt, alice):
    value = 1000*10**18;

    aliceBeforeBalance = usdt.balanceOf(alice)
    assert aliceBeforeBalance == 0

    tx = usdt._mint_for_testing(alice, value)
    assert tx.events[0].name == 'Transfer'

    assert tx.events['Transfer']['_value'] == value
    assert tx.events['Transfer']['_from'] == '0x0000000000000000000000000000000000000000'
    assert tx.events['Transfer']['_to'] == alice

    aliceAfterBalance = usdt.balanceOf(alice)
    assert aliceAfterBalance == value


