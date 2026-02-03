class UTXOManager:
        
        def __init__(self): #constructor
            self.utxo_set={}

        def add_utxo(self,tx_id:str,index:int,amount:float,owner:str):
            self.utxo_set[(tx_id,index)]={"amount":amount,"owner":owner}

        def remove_utxo(self,tx_id:str,index:int): #removes UTXOs which are used or not required
            self.utxo_set.pop((tx_id,index),None)

        def get_balance(self,owner:str)->float: #returns the balance of a user
            balance=0
            for temp_pull in self.utxo_set.values():
                if (temp_pull["owner"]==owner):
                    balance=balance+temp_pull["amount"]
            return balance
                            
        def exists(self,tx_id:str,index:int)->bool: # verifies the existence of a user in the chain
            return (tx_id,index) in self.utxo_set
            
        def get_utxos_for_owner(self,owner:str)->list: #
            utxos_list=[]
            for temp_val_key,temp_pull_val in self.utxo_set.items():
                if (temp_pull_val["owner"]==owner):
                    temp_tx_id, temp_index=temp_val_key
                    utxos_list.append((temp_tx_id,temp_index,temp_pull_val["amount"]))
            return utxos_list
        
        def get_utxo_amount(self,tx_id:str,index:int)->float:
            return self.utxo_set[(tx_id,index)]["amount"]
        
        def get_utxo_owner(self,tx_id:str,index:int)->str:
            return self.utxo_set[(tx_id,index)]["owner"]
        
        def utxo_clear(self):
            self.utxo_set={}
        
            
        
