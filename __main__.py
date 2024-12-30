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
