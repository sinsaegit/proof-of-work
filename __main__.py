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
    

    
class BlockchainInteraction:
    pass

if __name__ == "__main__":
    program = BlockchainInteraction()
    program.run()
