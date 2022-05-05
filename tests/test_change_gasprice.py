import brownie
from brownie.network import gas_price

def test_change_gasprice(exampleContract):
    beforeGasPrice = exampleContract.currentGasPrice()
    assert beforeGasPrice == 0

    gas_price("65 gwei")
    exampleContract.getVestingToken()

    afterGasPrice = exampleContract.currentGasPrice()
    assert afterGasPrice == 65000000000


