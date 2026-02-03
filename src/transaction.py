import time
import random
from validator import validator, validator_double_spend

def make_transaction(transaction,owner,receiver,transaction_amount, mempool,utxo_manager,transaction_fee=0.001):

    if transaction_amount<=0:
        print("Rejected: Negative or zero amount")
        return False

    validity,balance=validator(owner,transaction_amount,transaction_fee,utxo_manager,transaction)

    if not validity:
        print("Rejected: Insufficient funds")
        return False

    if not validator_double_spend(mempool,transaction):
        return False

    tx_id=f"{owner}_{receiver}_{random.randint(0,999)}"

    tx={
        tx_id:{
            "transaction_data":{
                "time": time.time(),
                "inputs": [{"prev_utxo": transaction,"owner": owner,"transaction_fee": transaction_fee}],
                "outputs": [{"amount": transaction_amount, "address": receiver},{"amount": balance - transaction_amount - transaction_fee,"address": owner}]
            }
        }
    }

   # Add to mempool
    change=mempool.add_mempool(tx)
    tx_id = list(tx.keys())[0]
    print("\nCreating transaction: ")
    print(f"Transaction valid! Fee: {transaction_fee} BTC")
    print(f"Transaction ID: {tx_id}")

    if change:
       print("Transaction added to mempool.")
       print(f"Mempool now has {len(mempool.transactions)} transactions.\n")
       return True
    else:
      print("Transaction rejected by mempool.\n")
      return False


