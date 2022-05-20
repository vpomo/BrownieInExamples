from brownie import Wei
import brownie

def test_payable_function(exampleContract, alice):
    before = exampleContract.myEther()
    assert before == 0

    value = Wei('1 ether')/5
    exampleContract.receiveEther({'from': alice, 'value': value})

    after = exampleContract.myEther()
    assert after == value



