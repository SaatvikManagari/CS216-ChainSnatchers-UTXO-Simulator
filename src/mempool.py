class Mempool:
    def __init__(self, max_size=50):
        self.transactions = []
        self.spent_utxos = set()
        self.max_size = max_size

    def add_mempool(self, tx):
        tx_id = list(tx.keys())[0]
        inputs = tx[tx_id]["transaction_data"]["inputs"]

        for i in inputs:
            for utxo in i["prev_utxo"]:
                if utxo in self.spent_utxos:
                    print("Rejected: First-seen rule (UTXO already used)")
                    return False

        self.transactions.append(tx)
        for i in inputs:
            for utxo in i["prev_utxo"]:
                self.spent_utxos.add(utxo)
        return True

    def mempool_out(self):
        return [list(tx.values())[0]["transaction_data"]
                for tx in self.transactions]

    def get_top_transactions(self, n):
        return sorted(
            self.transactions,
            key=lambda tx:
                tx[list(tx.keys())[0]]
                ["transaction_data"]["inputs"][0]["transaction_fee"],
            reverse=True
        )[:n]

    def remove_transaction(self, tx_id):
        for i, tx in enumerate(self.transactions):
            if tx_id in tx:
                inputs = tx[tx_id]["transaction_data"]["inputs"]
                for inp in inputs:
                    for utxo in inp["prev_utxo"]:
                        self.spent_utxos.discard(utxo)
                self.transactions.pop(i)
                return

    def clear(self):
        self.transactions.clear()
        self.spent_utxos.clear()
