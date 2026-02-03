from utxo_manager import UTXOManager
from mempool import Mempool
from validator import validator, validator_double_spend
from transaction import make_transaction
from block import mine_block
from test_scenarios import run_test_case


def print_genesis():
    print("=== Bitcoin Transaction Simulator ===")
    print("Initial UTXOs ( Genesis Block ) :")
    print("- Alice : 50.0 BTC")
    print("- Bob : 30.0 BTC")
    print("- Charlie : 20.0 BTC")
    print("- David : 10.0 BTC")
    print("- Eve : 5.0 BTC")
    print()

def view_utxo_set(utxo_manager, mining_done):
    print("\nUTXO SET:")

    for (tx_id,idx),data in utxo_manager.utxo_set.items():

        if mining_done and tx_id.startswith("genesis"):
            continue

        print(f"{tx_id}[{idx}] -> {data['owner']} : {data['amount']} BTC")

    print()

def print_balances(utxo_manager):
    print("\nUPDATED BALANCES: ")
    users = set()
    # Collect all known users from UTXO set
    for data in utxo_manager.utxo_set.values():
        users.add(data["owner"])

    for user in sorted(users):
        balance = utxo_manager.get_balance(user)
        print(f"{user} : {balance:.6f} BTC")

    print()



def view_mempool(mp):
    print("\MEMPOOL: ")
    for tx in mp.transactions:
        tx_id = list(tx.keys())[0]
        tx_data = tx[tx_id]["transaction_data"]
        fee = tx_data["inputs"][0]["transaction_fee"]
        print(f"TX ID: {tx_id}, Fee: {fee}")
    print()

def print_test_menu():
    print("\n=== Test Case Menu ===")
    print("1. Basic Valid Transaction")
    print("2. Multiple Inputs Transaction")
    print("3. Double-Spend in Same Transaction")
    print("4. Mempool Double-Spend")
    print("5. Insufficient Funds")
    print("6. Negative Amount")
    print("7. Zero Fee Transaction")
    print("8. Race Attack Simulation")
    print("9. Complete Mining Flow")
    print("10. Unconfirmed Chain")
    print("Enter test choice :", end=" ")



def select_utxos(utxo_manager, owner, amount, fee):

    #Returns list of (tx_id, index) or None if insufficient.
    utxos=utxo_manager.get_utxos_for_owner(owner)
    selected=[]
    total=0.0
    required=amount + fee

    for tx_id,idx,amt in utxos:
        selected.append((tx_id,idx))
        total+=amt
        if total>=required:
            return selected
    return None

def reset_block(utxo_manager:UTXOManager,mp:Mempool):
    mp.clear()
    utxo_manager.utxo_clear()
    utxo_manager.add_utxo("genesis_alice", 0, 50.0, "Alice")
    utxo_manager.add_utxo("genesis_bob", 0, 30.0, "Bob")
    utxo_manager.add_utxo("genesis_charlie", 0, 20.0, "Charlie")
    utxo_manager.add_utxo("genesis_david", 0, 10.0, "David")
    utxo_manager.add_utxo("genesis_eve", 0, 5.0, "Eve")

def is_valid_user(utxo_manager, user):
    for data in utxo_manager.utxo_set.values():
        if data["owner"]==user:
            return True
    return False


def main():
    # Initialize core components
    utxo_manager=UTXOManager()
    mp=Mempool()    
    mining_done=False
    genesis_displayed = False
    mp.clear()
    reset_block(utxo_manager,mp)
    while True:

        if not genesis_displayed:
            print_genesis()
            genesis_displayed = True
        else:
            print_balances(utxo_manager)

        print("Main Menu :")
        print("1. Create new transaction")
        print("2. View UTXO set")
        print("3. View mempool")
        print("4. Mine block")
        print("5. Run test scenarios")
        print("6. Exit")
        print()
        print("Enter choice :", end=" ")
        choice=input()

        if choice=="1":
            owner=input("Sender: ")
            receiver=input("Receiver: ")
            amount=float(input("Amount: "))
            fee=float(input("Transaction fee: "))
            if not is_valid_user(utxo_manager,owner):
                print("Invalid sender: address not found in system.\n")
                continue
            if not is_valid_user(utxo_manager,receiver):
                print("Invalid receiver: address not found in system.\n")
                continue

            if amount<=0:
               print("Amount must be positive.\n")
               continue

            if fee<0:
               print("Transaction fee cannot be negative.\n")
               continue

            selected_utxo=select_utxos(utxo_manager,owner,amount,fee)

            if not selected_utxo:
                print("Insufficient funds.\n")
                continue
            success = make_transaction(selected_utxo,owner,receiver,amount,mp,utxo_manager,fee)
            if success:
                print("Transaction added to mempool (pending).")
                print_balances(utxo_manager)
            else:
                print("Transaction failed.\n")

        elif choice=="2":
            view_utxo_set(utxo_manager,mining_done)

        elif choice=="3":
            view_mempool(mp)

        elif choice=="4":
            mine_block("Miner1", mp, utxo_manager)
            mining_done = True
            print_balances(utxo_manager)
            print()

        elif choice=="5":
            while True:        
                reset_block(utxo_manager,mp)                             
                print_test_menu()
                test_choice=input().strip()
                if test_choice=="11":
                    break
                run_test_case(test_choice,utxo_manager, mp)              

        elif choice=="6":
            print("Exiting simulator.")
            return

        else:
            print("Invalid choice.\n")


if __name__=="__main__":
    main()
