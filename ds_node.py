from node_final import Node
from constants import *
import hashlib

class DSNode (Node):

    # Python class constructor
    def __init__(self, host, port, n, delta, id=None, callback=None, max_connections=5):
        super(DSNode, self).__init__(host, port, id, callback, max_connections)
        self.pool = set()
        self.rounds = 2
        self.round_time = delta
        self.current_time = -1
        print("\033[93mLight Node: Started\033[0m")


    def node_message(self, node, data):
        """This method is invoked when a node send us a message.
            data is a string, need to convert to a message object
        """
        parts = str(data).split(":")
        messagebody = parts[0]
        type = int(parts[1])
        isBroadcast = parts[2]
        message_id = parts[3]
        num = parts[4]
        i = 1
        if (num & (1<<i)) == 0:
            num |= (1<<i)
        num_sign = bin(num).count('1')
        round_num = (self.current_time)/(self.round_time)

        if self.current_time == -1:
            self.start_protocol()
            print(messagebody)
        if num_sign == round_num :
            self.pool.add(messagebody)
            print(messagebody)
            self.send_to_nodes(Message(messagebody, type, isBroadcast, num), exclude=[node])
        
    def start_protocol(self):
        self.current_time = 0
        for current_round in range(self.rounds):
            self.current_time+=self.round_time
        if len(self.pool) == 1:
            print(next(iter(self.pool)))
        else :
            print("no message")
            # self.send_to_nodes(Message(next(iter(self.pool),5,False,0)))
        
    def outbound_node_connected(self, node):
        print("\033[93moutbound_node_connected {}: {}\033[0m".format(node.host, node.port))

    def inbound_node_connected(self, node):
        print("\033[93minbound_node_connected: {}: {}\033[0m".format(node.host, node.port))

    def inbound_node_disconnected(self, node):
        print("\033[93minbound_node_disconnected: {}: {}\033[0m".format(node.host, node.port))

    def outbound_node_disconnected(self, node):
        print("\033[93moutbound_node_disconnected: {}: {}\033[0m".format(node.host, node.port))

    def node_disconnect_with_outbound_node(self, node):
        print("\033[93mnode wants to disconnect with other outbound node: {}: {}\033[0m".format(node.host, node.port))

    def node_request_to_stop(self):
        print("\033[93mnode is requested to stop ({}):\033[0m".format(self.id))
