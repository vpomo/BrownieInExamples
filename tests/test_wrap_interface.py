import brownie

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

