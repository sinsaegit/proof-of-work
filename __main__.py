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

class BlockchainInteraction:
    pass

if __name__ == "__main__":
    program = BlockchainInteraction()
    program.run()
