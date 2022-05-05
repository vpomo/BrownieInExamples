import brownie
from brownie import chain, reverts

def test_change_time(chain, bob, exampleContract):
    value = 1000*10**18;
    bobBeforeBalance = exampleContract.balanceOf(bob)
    exampleContract.getVestingToken({'from': bob})

    with reverts("The last payment was less than a one day"):
        exampleContract.getVestingToken({'from': bob})

    chain.sleep(60*60*24 + 10)

    exampleContract.getVestingToken({'from': bob})
    bobAfterBalance = exampleContract.balanceOf(bob)

    assert bobAfterBalance - value * 2 == bobBeforeBalance


