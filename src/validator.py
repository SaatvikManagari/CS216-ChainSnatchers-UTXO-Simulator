from utxo_manager import UTXOManager
from mempool import Mempool

def validator(owner,transtion_amount,transaction_fee,utxo_manager,transaction):
    # Test 3: Same UTXO twice
    if len(transaction)!=len(set(transaction)):
        print(" Rejected: Double-spend inside same transaction")
        return False, 0

    balance_utxo=0
    for tx_id, index in transaction:
        if not utxo_manager.exists(tx_id,index):
            return False,0
        if utxo_manager.get_utxo_owner(tx_id,index)!=owner:
            return False,0
        balance_utxo+=utxo_manager.get_utxo_amount(tx_id,index)

    if balance_utxo<transtion_amount+transaction_fee:
        return False,0

    return True,balance_utxo


def validator_double_spend(mempool: Mempool,transaction: list[tuple[str, int]])->bool:
    mempool_history=mempool.mempool_out()

    for tx in mempool_history:
        for inp in tx["inputs"]:
            # Correct key: prev_utxo
            for used_utxo in inp["prev_utxo"]:
                if used_utxo in transaction:
                    print("Rejected: Double spend detected in mempool")
                    return False

    return True