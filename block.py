import time

def mine_block(miner_address, mempool, utxo_manager, num_txs=5):
    txs = mempool.get_top_transactions(num_txs)
    if not txs:
        print("No transactions to mine")
        return

    total_fee = 0.0

    for tx in txs:
        tx_id = list(tx.keys())[0]
        data = tx[tx_id]["transaction_data"]

        for inp in data["inputs"]:
            total_fee += inp["transaction_fee"]
            for utxo in inp["prev_utxo"]:
                utxo_manager.remove_utxo(*utxo)

        for idx, out in enumerate(data["outputs"]):
            utxo_manager.add_utxo(tx_id, idx,
                                 out["amount"], out["address"])

        mempool.remove_transaction(tx_id)
        print(f"Mined transaction: {tx_id}")

    utxo_manager.add_utxo(
        f"reward_{int(time.time())}", 0, total_fee, miner_address
    )
    print(f"Miner rewarded {total_fee} BTC")
