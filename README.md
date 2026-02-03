# CS216-ChainSnatchers-UTXO-Simulator

## Overview :

This project is a **simplified Bitcoin Transaction & UTXO Simulator** built as part of **CS 216: Introduction to Blockchain**. It demonstrates how Bitcoin’s **UTXO model**, **transaction validation**, **mempool**, **mining**, and **double-spending prevention** work — all in a local, non-distributed environment.

The simulator follows the assignment specification strictly and provides a **menu-driven CLI interface** to create transactions, mine blocks, and run mandatory test scenarios.

---

## Learning Objectives

* Understand the **UTXO (Unspent Transaction Output) model**
* Implement **Bitcoin-style transaction validation rules**
* Simulate **mempool conflict detection** and **double-spend prevention**
* Demonstrate the **transaction lifecycle** from creation to confirmation
* Understand **miner incentives and transaction fees**

---

## 🧱 Project Structure

```
CS216-UTXO-Simulator/
│
├── src/
│   ├── main.py              # Entry point & CLI menu
│   ├── utxo_manager.py      # UTXO management logic
│   ├── transaction.py      # Transaction structure
│   ├── validator.py        # Transaction validation rules
│   ├── mempool.py           # Mempool management
│   └── block.py             # Mining simulation
│
├── tests/
│   └── test_scenarios.py    # Mandatory test cases
│
├── sample_output.txt        # Sample program run output
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## Requirements to Run 

* **Python 3.8+**
* Standard Python libraries

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/SaatvikManagari/CS216-ChainSnatchers-UTXO-Simulator
cd CS216-ChainSnatchers-UTXO-Simulator
```

2. Run the simulator:

```bash
python src/main.py
```

---

## Features Implemented

### Core Components

* **UTXO Manager** 

  * Add / remove UTXOs
  * Balance calculation per user
   
* **Transaction Validation**

  * UTXO existence check
  * Double-spend prevention
  * Input–output balance check
  * Fee calculation
  * Negative amount rejection
    
* **Mempool**

  * Conflict detection
  * Fee-based transaction selection
    
* **Mining Simulation**

  * Confirms transactions
  * Updates UTXO set
  * Miner receives total fees
 
    
  The Repository consists of five source code files consisting of all the operations and the necessary management rules for the Blockchain each named after the 'section' in the Blockchain transaction process it deals with respectively . The file **main.py**  when run displays the genesis block with the all the owners in the system and the amount of bitcoin they own. It contains **10 different test cases** each specifically aims to understand how transactions work and how Double-spending / 'Illegal' spendings are dealt with in Blcokchain. 

 
---

## Genesis State

| Owner   | Balance (BTC) |
| ------- | ------------- |
| Alice   | 50.0          |
| Bob     | 30.0          |
| Charlie | 20.0          |
| David   | 10.0          |
| Eve     | 5.0           |

---

## Test Scenarios Covered

* Basic valid transaction
* Multiple-input transactions
* Double-spend in same transaction
* Mempool double-spend detection
* Insufficient funds
* Negative output amount
* Zero-fee transaction
* Race attack (first-seen rule)
* Complete mining flow
* Unconfirmed transaction chain (design choice documented in code)



---

## 🧠 Design Choices

* **In-memory storage** using Python dictionaries and sets
* **First-seen rule** for mempool conflict resolution
* **Reject spending of unconfirmed UTXOs** (simpler & explicitly documented)
* Clear error messages for all invalid cases
* Reject Transactions with owners / receivers not part of the system

---

## 👥 Team Information

**Team Name:** *Chain Snatchers*

| Name                     | Roll Number |
| ------------------------ | ----------- |
| Managari Saatvik         | 240002035   |
| Nemani Sandeep           | 240002044   |
| Nagalla Abhisri karthik  | 240002041   |
| Charan Malladi           | 240008016   |

---

## Notes

The Project is a **local simulation** of the Blockchain environment aiming to help understand the basic transaction politics 
and core Blockchain concepts like Mempool Management , UTXOS . No cryptography, networking, or consensus algorithms are used. 


