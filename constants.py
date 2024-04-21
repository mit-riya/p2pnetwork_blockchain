BLOCK = 1 
BLOCKCHAIN = 2 
TRANSACTION = 3
ACCESS = 4 

class Transaction:
    def __init__(self,index) -> None:
        self.index = index 
    def __str__(self):
        return f"Transaction #{self.index}"
    
class Message:
    def __init__(self,messagebody,type,message_id,isBroadcast = False):
        self.messagebody = messagebody
        self.type = type
        self.messageid = message_id
        self.isBroadcast = isBroadcast
        
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