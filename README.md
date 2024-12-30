# The TheoryCoin Project (a simple blockchain)

Everything you need to know about TheoryCoin  
*(This documentation is made to be easy-to-read and give an in-depth walkthrough of what TheoryCoin is all about).*

---

## Getting Started 
Before you start using the TheoryCoin program, we will give you a hands-on walkthrough of what the different methods and attributes mean. Since the source code is open source, you can easily interpret what the code implements.

The program consists of three main classes: **Block**, **TheoryCoin**, and **BlockchainInteraction**. The program allows users to mine blocks, review the blockchain, and exit the system.

---

## Classes

### 1. Block
- **Description**: This class represents the individual block. This scheme acts as a ruleset for how the TheoryCoin-class implements a block in the blockchain.
- **Attributes**:
  - `Timestamp`: The timestamp is created with `time.asctime()` in the exact moment the block is created.
  - `Height`: The position of the block in the chain.
  - `Transactions`: A list of transactions stored in the block.
  - `Current hash`: The hash value of the current block’s data.
  - `Previous hash`: The hash value of the previous block in the chain.
  - `Nonce`: A random number generated with brute force in the proof-of-work process.

### 2. TheoryCoin
- **Description**: The TheoryCoin class represents the blockchain itself and all the methods/operations performed on it. It manages the creation of the blocks, including the genesis block, as well as handling the addition of transactions, proof-of-work calculations, and inspection of the chain.
- **Attributes**:
  - `tcchain`: A list to store the blocks forming the blockchain.
- **Methods**:
  - `add_block()`: Adds a new block to the blockchain with transactions and proof-of-work.
  - `add_genesis_block()`: Creates the initial block (genesis block) for the blockchain.
  - `add_transactions()`: Allows users to input transactions and returns them as a list.
  - `add_hash(block)`: Computes the hash of a block’s data.
  - `proof_of_work(a_tuple)`: Implements the proof-of-work algorithm to find a nonce that results in a valid hash.
  - `review_chain()`: Allows users to select and view specific blocks within the blockchain.

### 3. BlockchainInteraction
- **Description**: The BlockchainInteraction class is responsible for user interaction. It provides a text-based menu for users to mine blocks, review the blockchain, or exit the program.
- **Attributes**:
  - `blockchain`: An instance of the TheoryCoin class to manage the blockchain.
  - `choices`: A dictionary mapping user menu choices to corresponding methods.
- **Methods**:
  - `greetings()`: Displays a welcome message with a loading animation.
  - `display_menu()`: Prints the menu options for the user.
  - `run()`: Main program loop for user interaction.
  - `opt1()`: Executes the option to mine a new block.
  - `opt2()`: Executes the option to review the blockchain.
  - `exit()`: Exits the program with a thank-you message.

---

## Blockchain Structure
- The Blockchain is represented as a list of blocks in the TheoryCoin class. The variable `self.tcchain` is initialized as soon as the program starts.
- Each block contains a timestamp, height, transaction data, current hash, previous hash, and nonce.
- The Genesis block is created first and has a predefined previous hash value of 64 `0`s.
- Subsequent blocks link to the previous block’s hash, creating a chain.

---

## Hashing
- Hashing is implemented using the Python library `hashlib`.
- The `add_hash()` method computes the hash of a block’s data. If no block has been mined, the program takes this into account and hashes based on fewer attributes.
- The `add_hash()` method works as a preliminary step before a tuple containing a temporary string and hash is sent to the `proof_of_work()` method.

---

## Proof-of-Work
- Proof-of-work is implemented to find a nonce that results in a hash with a specific pattern (in this case, `0000` at the beginning).
- The `proof_of_work()` method iterates through nonce values until a valid hash is found. It starts from 0 and increments until the condition is met.
- The nonce value is included in the block for verification.
- This process ensures all cases of finding `0000` are accounted for, reducing errors.

---

## User Interaction
- The BlockchainInteraction class provides a user-friendly text-based interface.
- When running the script:
  - An object `program` is created in the BlockchainInteraction class.
  - `program.run()` calls the interactive loop that contains the interface, greeting message, loading screen, and action menu.
- Users can:
  - Mine new blocks and optionally add transactions.
  - Review the chain by selecting specific blocks.
  - Exit the program.
- Note: The loading screen may not work correctly in IDLE or Jupyter notebooks.

---

## Example Usage
1. **Start the Program**:
   ```bash
   python3 theorycoin.py
