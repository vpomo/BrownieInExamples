pragma solidity ^0.8.12;

import "OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/token/ERC20/ERC20.sol";
import "OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/token/ERC20/IERC20.sol";

contract BrownieInExamples is ERC20 {

    receive() external payable {
    }

    constructor(address alice) ERC20("ExampleToken", "EXT") {
        _mint(alice, 1_000_000e18);
    }

    function etherBalance() external view returns(uint256) {
        return address(this).balance;
    }
}
