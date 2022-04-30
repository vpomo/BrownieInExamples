import pytest
from brownie import Wei, ZERO_ADDRESS
from brownie_tokens import ERC20


@pytest.fixture(scope='function', autouse=True)
def shared_setup(fn_isolation):
    pass


@pytest.fixture(scope='module')
def deployer(accounts):
    return accounts[0]


@pytest.fixture(scope='module')
def alice(accounts):
    return accounts[1]


@pytest.fixture(scope='module')
def bob(accounts):
    return accounts[2]



@pytest.fixture(scope='module')
def dave(accounts):
    return accounts[3]


@pytest.fixture(scope="module")
def exampleContract(BrownieInExamples, deployer, alice):
    instanсe = BrownieInExamples.deploy(alice, {'from': deployer})
    return instanсe


@pytest.fixture(scope="module")
def usdt():
    return ERC20('USDT test', 'USDT', decimals = 6, success = None)
