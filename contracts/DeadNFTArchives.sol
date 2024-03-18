// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "solady/src/tokens/ERC1155.sol";
import "solady/src/utils/ReentrancyGuard.sol";

contract DeadNFTArchives is ERC1155, ReentrancyGuard {
    // Base URI for constructing token URIs
    string private _baseURI;

    // Event for URI updates, following the ERC1155 standard's recommendation
    event URI(string value, uint256 indexed id);

    constructor(string memory baseURI) ERC1155("") {
        setBaseURI(baseURI);
    }

    // Sets the base URI for constructing token URIs
    function setBaseURI(string memory baseURI) public {
        _baseURI = baseURI;
    }

    // A function to mint new tokens
    // `to` is the recipient of the NFT
    // `id` is the token ID chosen by the user
    // `amount` is the quantity to mint (ERC1155 supports fungible and non-fungible tokens)
    // `data` is additional data with no specified format
    function mint(address to, uint256 id, uint256 amount, bytes memory data) public nonReentrant {
        _mint(to, id, amount, data);
        emit URI(tokenURI(id), id);
    }

    // Constructs the URI for a given token ID
    function tokenURI(uint256 id) public view returns (string memory) {
        return string(abi.encodePacked(_baseURI, uint2str(id), ".json"));
    }

    // Override the uri function to return the constructed URI for each token ID
    function uri(uint256 id) public view override returns (string memory) {
        return tokenURI(id);
    }

    // Helper function to convert uint256 to string
    function uint2str(uint256 _i) internal pure returns (string memory _uintAsString) {
        if (_i == 0) {
            return "0";
        }
        uint256 j = _i;
        uint256 len;
        while (j != 0) {
            len++;
            j /= 10;
        }
        bytes memory bstr = new bytes(len);
        uint256 k = len;
        while (_i != 0) {
            k = k-1;
            uint8 temp = (48 + uint8(_i - _i / 10 * 10));
            bytes1 b1 = bytes1(temp);
            bstr[k] = b1;
            _i /= 10;
        }
        return string(bstr);
    }
}
