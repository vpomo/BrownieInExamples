
<h4 align="center">Brownie in examples</h4>


[Brownie Official Documents](https://eth-brownie.readthedocs.io/en/stable/index.html)

### 1. How to transfer ether

#### tarnsfer to user
```solidity
from brownie import Wei
import brownie

def test_transfer_ether_to_user(accounts):
    value = Wei('1 ether')/5

    balanceBefore = accounts[1].balance()
    tx = accounts[2].transfer(accounts[1], amount = value)
    balanceAfter = accounts[1].balance()

    assert balanceBefore + value == balanceAfter
```

#### tarnsfer to contract
```solidity
def test_transfer_ether_to_contract(accounts, exampleContract):
    value = Wei('1 ether')/5

    balanceBefore = exampleContract.etherBalance()
    tx = accounts[2].transfer(exampleContract, amount = value)
    balanceAfter = exampleContract.etherBalance()

    assert balanceBefore + value == balanceAfter
```

pipx inject eth-brownie brownie-token-tester

