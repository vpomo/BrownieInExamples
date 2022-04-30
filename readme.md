
<h4 align="center">Brownie in examples</h4>


[Docs](https://eth-brownie.readthedocs.io/en/stable/index.html)

### 1. How to transfer ether

```solidity
from brownie import Wei
import brownie

def test_transfer_ether(accounts, interface, my_contract):
    value = Wei('1 ether')/5

    balanceBefore = accounts[1].balance()
    tx = accounts[2].transfer(accounts[1], amount = value)
    balanceAfter = accounts[1].balance()
    
assert b

   
```

    ```javascript
    
        IWETH(weth).deposit{value: repay_amount}();
        // It shoud repay to pair not router!
        IWETH(weth).transfer(pair, repay_amount);
   
    ```
