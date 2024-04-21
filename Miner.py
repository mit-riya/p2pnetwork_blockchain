from node import Node
from constants import *
import hashlib

class Miner (Node):

    # Python class constructor
    def __init__(self, host, port, id=None, hash_chain=[], transactionpool =[], callback=None, max_connections=5):
        super(Miner, self).__init__(host, port, id, callback, max_connections)
        print("Miner: Started")
        self.hash_chain = hash_chain 
        self.transactionpool = transactionpool
            
    def receive_chain(self, chain_string):
        # Parse the chain string and create block objects
        blocks_data = chain_string.strip().split('\n')
        self.hash_chain = []
        for block_data in blocks_data:
            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
            self.hash_chain.append(block_hash)
            
    def print_transaction_pool(self):
        for transaction in self.transactionpool:
            print(transaction)
            
    def display_chain(self):
        for block_hash in self.hash_chain:
            print(block_hash)
            
    
    def receive_data(self, transaction_string, rec_type):
        index = int(transaction_string.split('#')[1].strip())        
        if(int(rec_type) == TRANSACTION):
            transaction = Transaction(index)
            self.transactionpool.append(transaction)
        elif(int(rec_type) == BLOCK):
            block = Block(index)
            block_data = str(block)
            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
            self.hash_chain.append(block_hash)
            
    def add_block(self, block):
            block_data = str(block)
            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
            self.hash_chain.append(block_hash)

    def outbound_node_connected(self, node):
        print("outbound_node_connected (" + self.id + "): " + node.id)
        
    def inbound_node_connected(self, node):
        print("inbound_node_connected: (" + self.id + "): " + node.id)

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: (" + self.id + "): " + node.id)

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: (" + self.id + "): " + node.id)

    def node_message(self, node, data):
        """This method is invoked when a node send us a message.
            data is a string, need to convert to a message object
        """
        """ for miner It will ignore if some one request some data from it """
        
        self.debug_print("node_message: " + node.id + ": " + str(data))
        # print(data)
        parts = str(data).split(":")
        messagebody = parts[0]
        type = parts[1]
        isBroadcast = parts[2]
        message_id = int(parts[3])

        if int(type) == BLOCKCHAIN: 
            self.receive_chain(messagebody)
            self.display_chain()
        elif int(type) == TRANSACTION:
            self.receive_data(messagebody,type)
            print("Transaction received")
            print(messagebody)
        elif int(type) == BLOCK:
            self.receive_data(messagebody,type)
            print("Block received")
            print(messagebody)
        elif int(type) == ACCESS:
            self.send_to_node(node ,Message("I am not a full node", INFO , False))
        elif int(type) == INFO:
            print(messagebody + " from " + node.id)

        if isBroadcast == "True":
            if message_id not in self.broadcasted_messages:
                self.broadcasted_messages.add(message_id)
                self.send_to_nodes(data, exclude=[node])
        
    def node_disconnect_with_outbound_node(self, node):
        print("node wants to disconnect with oher outbound node: (" + self.id + "): " + node.id)
        
    def node_request_to_stop(self):
        print("node is requested to stop (" + self.id + "): ")
