import sys
import time
import socket
sys.path.insert(0, '..') # Import the files where the modules are located


from Miner import Miner
from Full_node import FullNode
from Light_node import LightNode
from constants import *

def get_ip_address():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to a remote server (doesn't have to be reachable)
        s.connect(("8.8.8.8", 80))
        # Get the local IP address
        ipv4_address = s.getsockname()[0]
        return ipv4_address
    except Exception as e:
        print("Error occurred while getting IPv4 address:", e)
        return None

def full_node():
    ip = get_ip_address()
    print("\033[94m" + f"Your ip is {ip}\n" + "\033[0m")

    node_1 = FullNode(ip, 8001 , chain= [Block.create_genesis_block(), Block(1), Block(2)])
    node_1.start()
    while(True):
        print("\033[94mPress 1 to request access to the blockchain\033[0m")
        print("\033[94mPress 2 to broadcast a transaction\033[0m")
        print("\033[94mPress 3 to connect to node\033[0m")
        print("\033[94mPress 4 to stop the node\033[0m")
        print("\033[94mPress 5 to display the chain\033[0m")

        choice = int(input())
        
        if choice == 1:
            node_1.send_to_nodes(Message("Request access to the blockchain", ACCESS , False))
        elif choice == 2:
            node_1.send_to_nodes(Message(Transaction(), TRANSACTION , True))
        elif choice == 3:
            ip = input("\033[94mEnter the IP address of the node you want to connect to\n\033[0m")
            node_1.connect_with_node(ip , 8001)
        elif choice == 4:
            node_1.stop()
            break
        elif choice == 5:
            node_1.display_chain()  
    print('Left the blockchain')
    
def miner():
    ip = get_ip_address()
    print("\033[92m" + f"Your ip is {ip}\n" + "\033[0m")
    node_1 = Miner(ip, 8001)
    node_1.start()
    while(True):
        print("\033[92mPress 1 to request access to the blockchain\033[0m")
        print("\033[92mPress 2 to broadcast a transaction\033[0m")
        print("\033[92mPress 3 to connect to node\033[0m")
        print("\033[92mPress 4 to stop the node\033[0m")
        print("\033[92mPress 5 to display the chain\033[0m")
        print("\033[92mPress 6 to broadcast a block\033[0m")
        print("\033[92mPress 7 to get transactions pool\033[0m")

        choice = int(input())
        
        if choice == 1:
            node_1.send_to_nodes(Message("Request access to the blockchain", ACCESS , False))
        elif choice == 2:
            node_1.send_to_nodes(Message(Transaction(), TRANSACTION , True))
        elif choice == 3:
            ip = input("\033[92mEnter the IP address of the node you want to connect to\n\033[0m")
            node_1.connect_with_node(ip , 8001)
        elif choice == 4:
            node_1.stop()
            break
        elif choice == 5:
            node_1.display_chain()  
        elif choice == 6:
            block_number = int(input("\033[92mEnter the block number\033[0m"))
            node_1.add_block(Block(block_number))
            node_1.send_to_nodes(Message(Block(block_number), BLOCK , True))
        elif choice == 7:
            node_1.print_transaction_pool()
    print('Left the blockchain')
    
    
    
def light_node():
    ip = get_ip_address()
    print("\033[91m" + f"Your ip is {ip}\n" + "\033[0m")
    node_1 = LightNode(ip, 8001)
    node_1.start()

    while(True):
        print("\033[91mPress 1 to request access to the blockchain\033[0m")
        print("\033[91mPress 2 to broadcast a transaction\033[0m")
        print("\033[91mPress 3 to connect to a node\033[0m")
        print("\033[91mPress 4 to stop the node\033[0m")
        print("\033[91mPress 5 to display the chain\033[0m")

        
        choice = int(input())
        
        if choice == 1:
            node_1.send_to_nodes(Message("Request access to the blockchain", ACCESS ,  False))
        elif choice == 2:
            node_1.send_to_nodes(Message(Transaction(), TRANSACTION , True))
        elif choice == 3:
            ip = input("\033[91mEnter the IP address of the node you want to connect to\n\033[0m")
            node_1.connect_with_node(ip , 8001)
        elif choice == 4:
            node_1.stop()
            break
        elif choice == 5:
            node_1.display_chain()
    print('Left the blockchain')

n = int(input("Enter 0 for full node, 1 for miner, 2 for light node\n"))
if n==0:
    full_node()
elif n==1:
    miner()
elif n==2:
    light_node()
    
