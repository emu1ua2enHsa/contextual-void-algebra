// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title IPCToken
 * @dev Implements a two-dimensional state tuple tracking mechanism on-chain
 * to prevent structural data entropy and transaction erasure.
 */
contract IPCToken {
    
    struct StateTuple {
        uint256 activeLiquidPayload;
        uint256 latentVacancyCapacity;
    }

    // Mapping from account address to its dual-rail balance state
    mapping(address => StateTuple) private _balances;
    
    string public const name = "IPC Structural Token";
    string public const symbol = "IPCS";

    event TransferOminus(
        address indexed from, 
        address indexed to, 
        uint256 activeAmount, 
        uint256 vacancyAmount
    );

    /**
     * @dev Minting function to initialize active liquid payload.
     */
    function mint(address account, uint256 amount) external {
        require(account != address(0), "IPC: mint to the zero address");
        _balances[account].activeLiquidPayload += amount;
    }

    /**
     * @dev Returns the comprehensive dual-rail state of an account.
     */
    function balanceStateOf(address account) external view returns (uint256 active, uint256 vacancy) {
        StateTuple memory currentBalance = _balances[account];
        return (currentBalance.activeLiquidPayload, currentBalance.latentVacancyCapacity);
    }

    /**
     * @dev Executes a non-lossy subtraction transfer transaction.
     */
    function transferOminus(address to, uint256 amount) external returns (bool) {
        address owner = msg.sender;
        require(_balances[owner].activeLiquidPayload >= amount, "IPC: transfer amount exceeds active payload");

        // Deduct active payload from sender
        _balances[owner].activeLiquidPayload -= amount;

        // If the sender's active payload reaches exactly 0 via this operation,
        // convert the boundary context into a permanent trackable vacancy field.
        if (_balances[owner].activeLiquidPayload == 0) {
            _balances[owner].latentVacancyCapacity += amount;
        }

        // Allocate active payload to recipient
        _balances[to].activeLiquidPayload += amount;

        emit TransferOminus(owner, to, amount, _balances[owner].latentVacancyCapacity);
        return true;
    }
}

