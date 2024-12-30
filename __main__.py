import hashlib
import time

class Block:
    def __init__(self):
        self.timestamp = time.asctime()
        self.height = None
        self.transaction = None
        self.current_hash = None
        self.previous_hash = None
        self.nonce = None

class TheoryCoin:
    def __init__(self):
        self.tcchain = []

    def add_block(self):
        if not self.tcchain:
            self.tcchain.append(self.add_genesis_block())
        else:
            block = Block()
            block.transaction = self.add_transactions()
            block.height = len(self.tcchain)
            block.previous_hash = self.tcchain[-1].current_hash
            hash_res = self.add_hash(block)
            pow_res = self.proof_of_work(hash_res)
            block.current_hash = pow_res[0]
            block.nonce = pow_res[1]
            self.tcchain.append(block)


    def add_genesis_block(self):
        genesis = Block()
        genesis.height = 0
        genesis.previous_hash = "0"*64
        genesis.transaction = self.add_transactions()
        hash_res = self.add_hash(genesis)
        pow_res = self.proof_of_work(hash_res)
        genesis.current_hash = pow_res[0]
        genesis.nonce = pow_res[1]
        return genesis
    

    def add_transactions(self):
        transactions = []
        while True:
            inp = str(input("\nWould you like to add a transaction? [y/n] >>> "))
            if inp == "y":
                print("\nPlease enter the following on the form (sender, recipient, value/msg)")
                sender = str(input("Add sender >>> "))
                recipient = str(input("Add recipient >>> "))
                value = str(input("Value >>> "))
                transactions.append((sender, recipient, value))
            elif inp == "n":
                break
            else:
                print("\nPlease choose a valid input")
                break
        return transactions
    
    def add_hash(self, block):
        if len(self.tcchain) == 0:
            temp_str = (str(block.timestamp) 
                    + str(block.transaction))
        else:
            temp_str = (
                str(block.timestamp)
                + str(block.height)
                + str(block.transaction)
                + str(block.previous_hash)
            )
        temp_hash = hashlib.sha256(temp_str.encode()).hexdigest()
        return temp_str, temp_hash


    def proof_of_work(self, a_tuple):
        if a_tuple[1][:4] == "0000":
            return a_tuple[1], 0
        else:
            nonce = 0
            temp_hash = "0"
            while temp_hash[:4] != "0000":
                temp_hash = hashlib.sha256((a_tuple[0] + str(nonce)).encode()).hexdigest()
                nonce += 1
            print(f"Hashed value: {temp_hash} - Nonce: {nonce}")
            return temp_hash, nonce

    def review_chain(self):
        chain = [obj for obj in range(len(self.tcchain))]
        if len(chain) > 9:
            print("\n", ["..."]+[chain[-9:]])
        else:
            print(f"\nCurrent chain: {chain}")

        while True:
            inp = int(input("Which block do you wish to review? >>> "))
            if 0<=inp<=len(self.tcchain):
                self.print_block(self.tcchain[inp])
                break
            elif len(self.tcchain) == 0:
                print("There are no blocks mined")
                break
            else:
                print("Please select a valid block")
                continue

    def print_block(self, block):
        print(f"\n\n--------------- TheoryCoin Block No. {block.height} ---------------")
        print(f"\nMined on (timestamp): {block.timestamp},"\
        f"\nCurrent hash: {block.current_hash},"\
        f"\nPrevious hash: {block.previous_hash},"\
        f"\nNonce value: {block.nonce},"\
        f"\nList of transactions:")
        for num,i in enumerate(block.transaction):
            print(f"\tTransaction no.{num+1}:")
            print(f"\t\t\tSender: {i[0]}, \n\t\t\tRecipient: {i[1]}, \n\t\t\tValue: {i[2]}")
        print("------------------------------------------------------------------\n")
        # obj = {
        #     "height":block.height,1
        #     "timestamp":block.timestamp,
        #     "transactions":block.transaction,
        #     "current_hash":block.current_hash,
        #     "previous_hash":block.previous_hash,
        #     "nonce":block.nonce
        # }
        # print(str(obj))

class BlockchainInteraction:
    pass

if __name__ == "__main__":
    program = BlockchainInteraction()
    program.run()
