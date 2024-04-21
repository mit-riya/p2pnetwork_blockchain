from node import Node
from constants import *
import hashlib

class LightNode (Node):

    # Python class constructor
    def __init__(self, host, port, id=None, chain=[], callback=None, max_connections=5):
        super(LightNode, self).__init__(host, port, id, chain, callback, max_connections)
        self.chain = chain 
        print("Light Node: Started")

    def receive_chain(self, chain_string):
        # Parse the chain string and create block objects
        blocks_data = chain_string.strip().split('\n')
        self.chain = []
        for block_data in blocks_data:
            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
            self.chain.append(block_hash)

    def receive_data(self, transaction_string, rec_type):
        # Parse the chain string and create block objects
        # blocks_data = chain_string.strip().split('\n')
        # self.chain = []
        # for block_data in blocks_data:
        index = int(transaction_string.split('#')[1].strip())

        if(rec_type == BLOCK):
            block = str(Block(index))
            block_hash = hashlib.sha256(block.encode()).hexdigest()
            self.chain.append(block_hash)

    def node_message(self, node, data):
        """This method is invoked when a node send us a message.
            data is a string, need to convert to a message object
        """
        self.debug_print("node_message: " + node.id + ": " + str(data))
        parts = str(data).split(":")
        messagebody = parts[0]
        type = int(parts[1])
        isBroadcast = parts[2]
        print(parts[3])
        message_id = parts[3]

        print("Message Structure starts")
        print(messagebody)
        print(type)
        print(isBroadcast)
        print(message_id)
        print("Message Structure ends")
        
        if type == BLOCKCHAIN: 
            self.receive_chain(chain_string = messagebody)
            self.display_chain()
        elif type == BLOCK:
            self.receive_data(messagebody,type)
            print("Block received")
            print(messagebody)
        elif type == ACCESS:
            self.send_through_id(node.id ,Message("I am not a full node", INFO , False))
        elif type == INFO:
            print(messagebody + " from " + node.id)
        # else:
        #     print("Invalid message type")
        if isBroadcast:
            if message_id not in self.broadcasted_messages:
                self.broadcasted_messages.add(message_id)
                self.send_to_nodes(data, exclude=[node])
            
        # if self.callback is not None:
        #     self.callback("node_message", self, node, data)

    def display_chain(self):
        for block in self.chain:
            print(block)

    def outbound_node_connected(self, node):
        print("outbound_node_connected (" + self.id + "): " + node.id)
        
    def inbound_node_connected(self, node):
        print("inbound_node_connected: (" + self.id + "): " + node.id)

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: (" + self.id + "): " + node.id)

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: (" + self.id + "): " + node.id)
    
    def node_disconnect_with_outbound_node(self, node):
        print("node wants to disconnect with oher outbound node: (" + self.id + "): " + node.id)
        
    def node_request_to_stop(self):
        print("node is requested to stop (" + self.id + "): ")
        
        