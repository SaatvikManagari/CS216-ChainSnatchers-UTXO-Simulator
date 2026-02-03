from transaction import make_transaction
from block import mine_block

def run_test_case(case_no, utxo, mp):

    match case_no:

        case "1":
            print("\n[Test 1] Basic Valid Transaction")
            make_transaction([("genesis_alice", 0)],"Alice", "Bob", 10,mp, utxo)

        case "2":
            print("\n[Test 2] Multiple Inputs Transaction")
            utxo.add_utxo("bonus_alice", 0, 20, "Alice")
            utxo.add_utxo("bonus_alice", 0, 50, "Alice")
            make_transaction([("genesis_alice", 0), ("bonus_alice", 0)], "Alice", "Bob", 60,mp, utxo)

        case "3":
            print("\n[Test 3] Double-Spend in Same Transaction")
            make_transaction([("genesis_bob", 0), ("genesis_bob", 0)],"Bob", "Charlie", 10,mp, utxo)

        case "4":
            print("\n[Test 4] Mempool Double-Spend")
            make_transaction([("genesis_charlie", 0)],"Alice", "Bob", 5,mp, utxo)
            make_transaction([("genesis_charlie", 0)],"Alice", "Charlie", 5,mp, utxo)

        case "5":
            print("\n[Test 5] Insufficient Funds")
            make_transaction([("genesis_bob", 0)],"Bob", "Alice", 35,mp, utxo)

        case "6":
            print("\n[Test 6] Negative Amount")
            make_transaction([("genesis_david", 0)],"David", "Bob", -5,mp, utxo)

        case "7":
            print("\n[Test 7] Zero Fee Transaction")
            make_transaction([("genesis_eve", 0)],"Eve", "Alice", 5,mp, utxo, 0)

        case "8":
            print("\n[Test 8] Race Attack (First-Seen Rule)")
            make_transaction([("genesis_alice", 0)],"Alice", "Merchant", 5,mp, utxo, 0.001)
            make_transaction([("genesis_alice", 0)],"Alice", "Attacker", 5,mp, utxo, 0.01)

        case "9":     
              make_transaction([("genesis_alice", 0)], "Alice", "Bob", 10,mp, utxo, 0.001)
              make_transaction([("genesis_bob", 0)],"Bob", "Charlie", 5,mp, utxo, 0.001)
              make_transaction([("genesis_charlie", 0)], "Charlie", "David", 3,mp, utxo, 0.001)
              print("\nMempool size before mining:", len(mp.transactions))

              print("\nMining block\n")
              mine_block("Miner1", mp, utxo)
   
              print("\n POST-MINING VERIFICATION")

              print("\nUpdated UTXO SET:")
              for (tx_id, idx), data in utxo.utxo_set.items():
                if not tx_id.startswith("genesis"):
                   print(f"{tx_id}[{idx}] -> {data['owner']} : {data['amount']} BTC")

              print("\nMiner balance:", utxo.get_balance("Miner1"), "BTC")
              print("Mempool size after mining:", len(mp.transactions))

        case "10":
            print("\n[Test 10] Unconfirmed Chain")
            print("Rejected by design: cannot spend unconfirmed UTXO")

        case _:
            print("Invalid test case.")