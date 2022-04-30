import brownie

def test_transfer_tokens_with_real_contract(alice, bob, exampleContract):
    value = 1000*10**18;

    aliceBeforeBalance = exampleContract.balanceOf(alice)
    bobBeforeBalance = exampleContract.balanceOf(bob)

    tx = exampleContract.transfer(bob, value, {'from': alice})

    aliceAfterBalance = exampleContract.balanceOf(alice)
    bobAfterBalance = exampleContract.balanceOf(bob)

    assert aliceBeforeBalance - value == aliceAfterBalance
    assert bobBeforeBalance + value == bobAfterBalance


def test_transfer_tokens_with_test_contract(alice, bob, usdt):
    value = 1000*10**18;

    usdt._mint_for_testing(alice, value)

    aliceBeforeBalance = usdt.balanceOf(alice)
    bobBeforeBalance = usdt.balanceOf(bob)

    tx = usdt.transfer(bob, value, {'from': alice})

    aliceAfterBalance = usdt.balanceOf(alice)
    bobAfterBalance = usdt.balanceOf(bob)

    assert aliceBeforeBalance - value == aliceAfterBalance
    assert bobBeforeBalance + value == bobAfterBalance
