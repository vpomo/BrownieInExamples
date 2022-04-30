
<h4 align="center">Brownie in examples</h4>


[Brownie Official Documents](https://eth-brownie.readthedocs.io/en/stable/index.html)

---

##Table of contents

[1.1. transfer ether to user](transfer ether to user)

[1.2. transfer ether to contract](transfer ether to contract)

[2.1. transfer tokens with real contract](transfer tokens with real contract)

[2.2. transfer tokens with test contract](transfer tokens with test contract)


---
#### 1. How to transfer ether

##### 1.1. transfer ether to user
##### file tests/test_transfer_ether.py:
```python
def test_transfer_ether_to_user(accounts):
    value = Wei('1 ether')/5

    balanceBefore = accounts[1].balance()
    tx = accounts[2].transfer(accounts[1], amount = value)
    balanceAfter = accounts[1].balance()

    assert balanceBefore + value == balanceAfter
```

#### 1.2. transfer ether to contract

##### file tests/conftest.py:
```python
@pytest.fixture(scope="module")
def exampleContract(BrownieInExamples, deployer, alice):
    instanсe = BrownieInExamples.deploy(alice, {'from': deployer})
    return instanсe
```

##### file tests/test_transfer_ether.py:
```python
def test_transfer_ether_to_contract(accounts, exampleContract):
    value = Wei('1 ether')/5

    balanceBefore = exampleContract.etherBalance()
    tx = accounts[2].transfer(exampleContract, amount = value)
    balanceAfter = exampleContract.etherBalance()

    assert balanceBefore + value == balanceAfter
```

#### 2. How to transfer tokens

##### 2.1. transfer tokens with real contract

##### file tests/test_transfer_tokens.py:
```python
def test_transfer_tokens_with_real_contract(alice, bob, exampleContract):
    value = 1000*10**18;

    aliceBeforeBalance = exampleContract.balanceOf(alice)
    bobBeforeBalance = exampleContract.balanceOf(bob)

    tx = exampleContract.transfer(bob, value, {'from': alice})

    aliceAfterBalance = exampleContract.balanceOf(alice)
    bobAfterBalance = exampleContract.balanceOf(bob)

    assert aliceBeforeBalance - value == aliceAfterBalance
    assert bobBeforeBalance + value == bobAfterBalance
```

##### 2.2. transfer tokens with test contract

pipx inject eth-brownie brownie-token-tester

##### file tests/conftest.py:
```python
@pytest.fixture(scope="module")
def usdt():
    return ERC20('USDT test', 'USDT', decimals = 6, success = None)
```

##### file tests/test_transfer_tokens.py:
```python
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
```

#### 3. How to interact with the interface

added 2 files:
interfaces/UniswapRouter.json
interfaces/UniswapPair.json

##### file brownie-config.yaml:
```
networks:
  default: mainnet-fork
```
##### file tests/test_transfer_tokens.py:
```python
def test_wrap_real_contract(interface):
    inAmount = 1000000
    reserveIn = 10e18
    reserveOut = 500e18

    uniswap = interface.UniswapRouter('0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D')
    outAmount = uniswap.getAmountOut(inAmount, reserveIn, reserveOut)
    assert outAmount == 49849999

    pair = interface.UniswapPair('0x9896BD979f9DA57857322Cc15e154222C4658a5a')
    totalSupply = pair.totalSupply()
    assert totalSupply == 4627357422247550
```

#### 3. How to interact with the interface



