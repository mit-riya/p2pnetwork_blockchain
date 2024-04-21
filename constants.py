BLOCK = 1 
BLOCKCHAIN = 2 
TRANSACTION = 3
ACCESS = 4 
INFO = 5

from datetime import datetime
import time

class Transaction:
    def __init__(self,index) -> None:
        self.index = index 
    def __str__(self):
        return f"Transaction #{self.index}"
    
class Message:
    def __init__(self,messagebody,type,isBroadcast = False):
        self.messagebody = messagebody
        self.type = type
        self.messageid = int(1000*time.time())
        self.isBroadcast = isBroadcast

    # def get_seconds_difference():
    #     # Define the specific date and time
    #     specific_datetime = datetime(year=2022, month=4, day=20, hour=12, minute=0)

    #     # Get the current date and time
    #     current_datetime = datetime.now()

    #     # Calculate the difference in seconds
    #     difference = (current_datetime - specific_datetime).total_seconds()

    #     return difference
    
    def getMessageBody(self):
        return self.messagebody
    def __str__(self):
        return f"{self.messagebody}:{self.type}:{self.isBroadcast}:{self.messageid}"

    # @classmethod
    # def from_string(cls, string):
        
class Block:
    def __init__(self, index):
        self.index = index

    @staticmethod
    def create_genesis_block():
        # Manually create the first block (genesis block)
        return Block(0)

    def __str__(self):
        return f"Block #{self.index}"