pragma solidity ^0.8.12;

contract BrownieInExamples {

    receive() external payable {
    }

    function etherBalance() external view returns(uint256) {
        return address(this).balance;
    }
}
