#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# This example show how to derive a own Node class (MyOwnPeer2PeerNode) from p2pnet.Node to implement your own Node   #
# implementation. See the MyOwnPeer2PeerNode.py for all the details. In that class all your own application specific  #
# details are coded.                                                                                                  #
#######################################################################################################################

import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
from constants import *
node_1 = MyOwnPeer2PeerNode("10.150.34.237", 8001, 1 ,  [Block.create_genesis_block(), Block(1), Block(2)])
# node_1 = MyOwnPeer2PeerNode("10.150.34.237", 8002, 2)
# node_3 = MyOwnPeer2PeerNode("10.20.1.105", 8003, 3)

# time.sleep(1)

node_1.start()
# node_2.start()
# node_3.start()

# time.sleep(1)

debug = True

# node_2.debug = debug
# node_3.debug = debug

# node_1.connect_with_node('10.20.1.105', 8002)
# node_2.connect_with_node('10.20.1.105', 8003)
# node_3.connect_with_node('10.20.1.105', 8001)

# time.sleep(2)

# node_1.send_to_nodes("message: Hi there!")


# node_1.send_to_nodes(node_1.get_chain_string())


# time.sleep(10)

# node_1.stop()
# time.sleep(10)
# node_2.stop()
# time.sleep(10)
# node_3.stop()




while(True):
    print("Press 1 to request access to the blockchain")
    print("Press 2 to broadcast a block")
    print("Press 3 to broadcast a transaction")
    print("Press 4 to stop the node")
    
    choice = int(input())
    
    if choice == 1:
        node_1.send_to_nodes(Message("Request access to the blockchain", ACCESS , 3 , False))
    elif choice == 2:
        node_1.send_to_nodes(Message(Block(3), BLOCK , 2 , True))
    elif choice == 3:
        node_1.send_to_nodes(Message(Transaction(1), TRANSACTION , 1 , True))
    elif choice == 7:
        node_1.connect_with_node("10.150.34.237" , 8002)
    elif choice == 4:
        node_1.stop()
        break
    elif choice == 5:
        print("Enter the node id to which you want to send the chain")
        id = int(input())
        node_1.send_through_id(id, Message(node_1.get_chain_string(), BLOCKCHAIN , 4 , False))
    
    
print('end test')