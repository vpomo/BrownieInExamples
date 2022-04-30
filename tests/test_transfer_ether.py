from brownie import Wei
import brownie

def test_transfer_ether_to_user(accounts):
    value = Wei('1 ether')/5

    balanceBefore = accounts[1].balance()
    tx = accounts[2].transfer(accounts[1], amount = value)
    balanceAfter = accounts[1].balance()

    assert balanceBefore + value == balanceAfter


def test_transfer_ether_to_contract(accounts, exampleContract):
    value = Wei('1 ether')/5

    balanceBefore = exampleContract.etherBalance()
    tx = accounts[2].transfer(exampleContract, amount = value)
    balanceAfter = exampleContract.etherBalance()

    assert balanceBefore + value == balanceAfter
