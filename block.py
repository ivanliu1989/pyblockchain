import hashlib as hasher
import uuid


class Block2(object):
    def __init__(self, data=None, previous_hash=None):
        self.identifier = uuid.uuid4().hex  # Generate unique identifier
        self.nonce = None  # nonce value
        self.data = data  # block data
        self.previous_hash = previous_hash  # parent hash value

    def hash(self, nonce=None):
        '''
        Calculate hash value
        '''
        message = hasher.sha256()
        message.update(self.identifier.encode('utf-8'))
        message.update(str(nonce).encode('utf-8'))
        message.update(str(self.data).encode('utf-8'))
        message.update(str(self.previous_hash).encode('utf-8'))
        return message.hexdigest()

    def hash_is_valid(self, the_hash):
        '''
        Check if hash is valid
        '''
        return the_hash.startswith('0000')

    def __repr__(self):
        return 'Block<Hash: {}, Nonce: {}>'.format(self.hash(self.nonce), self.nonce)

    def mine(self):
        # Initialise nonce
        cur_nonce = self.nonce or 0
        # Find valid hash value
        while True:
            the_hash = self.hash(nonce=cur_nonce)
            if self.hash_is_valid(the_hash):
                self.nonce = cur_nonce
                print("Find!")
                break
            else:
                cur_nonce += 1
                print("Not find")


class BlockChain(object):
    def __init__(self):
        self.head = None # Point to the latest block
        self.blocks = {} # A dict for all blocks
    '''
    Add new blocks
    '''
    def add_block(self,new_block):
        previous_hash = self.head.hash() if self.head else None
        new_block.previous_hash = previous_hash

        self.blocks[new_block.identifier] = {
            'block': new_block,
            'previous_hash': previous_hash,
            'previous': self.head
        }
        self.head = new_block

    def __repr__(self):
        num_existing_block = len(self.blocks)
        return 'Blockchian<{} Blocks, Head: {}>'.format(num_existing_block,
                                                        self.head.identifier if self.head else None)


block = Block2("Hello World!")
# block
# block.hash_is_valid(block.hash())
# block.hash(1)

# Start mining and being rich
block.mine()
block

# Initialize chain
chain = BlockChain()
chain
chain.add_block(block)

for i in range(6):
    new_block = Block2(i)
    new_block.mine()
    chain.add_block(new_block)

chain