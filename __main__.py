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
    def __init__(self):
        self.blockchain = TheoryCoin()
        self.choices = {
            "1":self.opt1,
            "2":self.opt2,
            "3":self.exit
        }

    def greetings(self):
        line = ("Welcome to TheoryCoinServices inc.,\n"\
            "The no.1 provider of ming services of TheoryCoin and related services.\n")

        def dotmove(n):
            dot = "."*n
            loading = (f"Loading {dot}")
            print(loading + "   ", end = '\r')
            time.sleep(0.18)

        for x in range(2):
            for y in range(4):
                dotmove(y)
            #for z in range(2,  0, -1):
            for z in range(4):
                dotmove(z)

        dotmove(3)
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.007)
        print("\n")
            
    def display_menu(self):
        print("\n ------- TheoryCoin -------")
        print("Current available choices")
        print("1. Mine a block")
        print("2. Review chain")
        print("3. Exit chain")

    def run(self):
        self.greetings()
        while True:
            self.display_menu()
            choice = input("Enter choice >>> ")
            if choice in self.choices:
                self.choices[choice]()
            else:
                print("\nPlease select a valid choice.")

    def opt1(self):
        self.blockchain.add_block()

    def opt2(self):
        self.blockchain.review_chain()

    def exit(self):
        import sys
        line = ("Thank you for using our services.\nGoodbye.")
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.007)
        print("\n")
        sys.exit(0)

if __name__ == "__main__":
    program = BlockchainInteraction()
    program.run()
