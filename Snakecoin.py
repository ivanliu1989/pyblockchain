import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        k = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(k.encode("utf8"))
        return sha.hexdigest()


import datetime as date


def create_genesis_block():
    '''
    Mannual construct a block with
    index zero and arbitary previous hash
    '''
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


# Initialize the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Definite the number of blocks to be added
num_of_blocks_to_add = 2000

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been added to the bloackchain! \n{}".format(block_to_add.index, block_to_add.hash))
