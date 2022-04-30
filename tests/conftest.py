import pytest
from brownie import Wei, ZERO_ADDRESS

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
def exampleContract(BrownieInExamples, deployer):
    instanсe = BrownieInExamples.deploy({'from': deployer})
    return instanсe
