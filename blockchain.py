import sys
import time
import socket
sys.path.insert(0, '..') # Import the files where the modules are located


from Miner import Miner
from Full_node import FullNode
from Light_node import LightNode
from constants import *

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def full_node():
    ip = get_ip_address()
    node_1 = FullNode(ip, 8001 , chain= [Block.create_genesis_block(), Block(1), Block(2)])
    node_1.start()
    while(True):
        print("Press 1 to request access to the blockchain")
        print("Press 2 to broadcast a transaction")
        print("Press 3 to connect to node")
        print("Press 4 to stop the node")
        print("Press 5 to display the chain")
        
        choice = int(input())
        
        if choice == 1:
            node_1.send_to_nodes(Message("Request access to the blockchain", ACCESS , False))
        elif choice == 2:
            node_1.send_to_nodes(Message(Transaction(), TRANSACTION , True))
        elif choice == 3:
            ip = input("Enter the ip address of the node you want to connect to")
            node_1.connect_with_node(ip , 8001)
        elif choice == 4:
            node_1.stop()
            break
        elif choice == 5:
            node_1.display_chain()  
        elif choice == 6:
            print("Enter the node id to which you want to send the chain")
            id = int(input())
            node_1.send_through_id(id, Message(node_1.get_chain_string(), BLOCKCHAIN , False)) 
    print('Left')
    
def miner():
    ip = get_ip_address()
    node_1 = Miner(ip, 8001)
    node_1.start()
    while(True):
        print("Press 1 to request access to the blockchain")
        print("Press 2 to broadcast a transaction")
        print("Press 3 to connect to node")
        print("Press 4 to stop the node")
        print("Press 5 to display the chain")
        print("Press 6 to broadcast a block")
        print("Press 7 to get transactions pool")
        
        choice = int(input())
        
        if choice == 1:
            node_1.send_to_nodes(Message("Request access to the blockchain", ACCESS , False))
        elif choice == 2:
            node_1.send_to_nodes(Message(Transaction(), TRANSACTION , True))
        elif choice == 3:
            ip = input("Enter the ip address of the node you want to connect to")
            node_1.connect_with_node(ip , 8001)
        elif choice == 4:
            node_1.stop()
            break
        elif choice == 5:
            node_1.display_chain()  
        elif choice == 6:
            node_1.add_block(Block(3))
            node_1.send_to_nodes(Message(Block(3), BLOCK , True))
        elif choice == 7:
            node_1.print_transaction_pool()
    print('Left')
    
    
    
def light_node():
    ip = get_ip_address()
    node_1 = LightNode(ip, 8003 ,3)
    node_1.start()

    while(True):
        print("Press 1 to request access to the blockchain")
        print("Press 2 to broadcast a transaction")
        print("Press 3 to connect to a node")
        print("Press 4 to stop the node")
        print("Press 5 to display the chain")
        
        choice = int(input())
        
        if choice == 1:
            node_1.send_to_nodes(Message("Request access to the blockchain", ACCESS ,  False))
        elif choice == 2:
            node_1.send_to_nodes(Message(Transaction(), TRANSACTION , True))
        elif choice == 3:
            ip = input("Enter the ip address of the node you want to connect to")
            node_1.connect_with_node(ip , 8001)
        elif choice == 4:
            node_1.stop()
            break
        elif choice == 5:
            node_1.display_chain()
        
        
    print('end test')

n = int(input("Enter 0 for full node, 1 for miner, 2 for light node"))
if n==0:
    full_node()
elif n==1:
    miner()
elif n==2:
    light_node()
    
