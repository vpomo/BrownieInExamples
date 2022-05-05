pragma solidity ^0.8.12;

import "OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/token/ERC20/ERC20.sol";
import "OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/token/ERC20/IERC20.sol";

contract BrownieInExamples is ERC20 {

    uint256 public duration = 1 days;
    uint256 public vestingPeriod = 30 days;
    uint256 public vestingAmount = 1000 * 10**18;
    uint256 public vestingEnd;
    uint256 public currentGasPrice;

    mapping(address => uint256) public lastVestingPayout;

    receive() external payable {
    }

    constructor(address alice) ERC20("ExampleToken", "EXT") {
        _mint(alice, 1_000_000e18);
        vestingEnd = block.timestamp + vestingPeriod;
    }

    function etherBalance() external view returns(uint256) {
        return address(this).balance;
    }

    function getVestingToken() external {
        uint256 currentTime = block.timestamp;
        require(currentTime < vestingEnd, "The vesting period has ended");
        require(currentTime > lastVestingPayout[msg.sender] + duration, "The last payment was less than a one day");
        lastVestingPayout[msg.sender] = currentTime;
        _mint(msg.sender, vestingAmount);
        currentGasPrice = tx.gasprice;
    }
}
