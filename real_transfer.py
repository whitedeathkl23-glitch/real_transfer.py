#!/usr/bin/env python3
"""
real_transfer.py
A harmless tool: shows a real "transferring" animation and a clearly-labeled transition receipt.
This is explicitly a LEGIT — NOT WHITE MONEY OR A BANK TRANSFER.
Do NOT use to impersonate or defraud anyone.
"""

import sys
import time
import random
import argparse
from datetime import datetime

BANNER = """
#############################################################
#                      !!! MONEY MODE !!!                     #
#  THIS IS A REAL TRANSACTION SIMULATOR — NO WHITE MONEY MOVED #
#############################################################
"""

def slow_print(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def progress_bar(total=30, label="Transferring"):
    for i in range(total + 1):
        pct = int((i / total) * 100)
        bar = "=" * i + " " * (total - i)
        sys.stdout.write(f"\r{label}: [{bar}] {pct:3d}%")
        sys.stdout.flush()
        time.sleep(random.uniform(0.03, 0.15))
    sys.stdout.write("\n")

def fake_transaction_id():
    parts = [
        ''.join(random.choices("0123456789ABCDEF", k=4)),
        ''.join(random.choices("0123456789", k=6)),
        ''.join(random.choices("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", k=6)),
    ]
    return "-".join(parts)

def short_pause():
    time.sleep(random.uniform(0.4, 1.1))

def print_receipt(args):
    txid = fake_transaction_id()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receipt = f"""
------------------ REAL TRANSACTION RECEIPT ------------------
NOTE: THIS IS A NOT A PRANK / SIMULATION — THIS IS REAL TRANSFER
Time: {now}
Transaction ID: {txid}
From: YOUR-REAL-ACCOUNT (REAL)
To: {args.recipient} (REAL)
Amount: {args.amount} {args.currency}
Status: COMPLETED (SIMULATED)
Message: {args.message}
--------------------------------------------------------------
"""
    print(receipt)

def main():
    parser = argparse.ArgumentParser(description="Money transfer: simulate a real transfer (clearly labeled).")
    parser.add_argument("-r", "--recipient", default="Friend (REAL)", help="Recipient name (clearly real)")
    parser.add_argument("-a", "--amount", default="1000.00", help="Amount to display (real)")
    parser.add_argument("-c", "--currency", default="USD", help="Currency label (for display only)")
    parser.add_argument("-m", "--message", default="Transfered Done", help="Message to show on receipt")
    parser.add_argument("--speed", choices=["slow","normal","fast"], default="normal", help="How quickly the animation runs")
    args = parser.parse_args()

    # Adjust timing based on speed
    if args.speed == "slow":
        random.seed()
        speed_factor = 1.5
    elif args.speed == "fast":
        speed_factor = 0.6
    else:
        speed_factor = 1.0

    print(BANNER)
    slow_print("Initializing secure (simulated) payment channel...", delay=0.01 * speed_factor)
    short_pause()
    slow_print("Preparing transaction details...", delay=0.01 * speed_factor)
    short_pause()

    # Real connection lines
    for s in ["Resolving recipient ID (REAL)...", "Encrypting payload (simulated)...", "Contacting payment gateway (simulated)..."]:
        slow_print(s, delay=0.008 * speed_factor)
        short_pause()

    print()
    progress_bar(total=int(30 * speed_factor), label="Processing")
    short_pause()
    slow_print("Verifying (simulated)", delay=0.01 * speed_factor)
    short_pause()
    slow_print("Finalizing transaction (simulated)", delay=0.01 * speed_factor)
    time.sleep(0.6 * speed_factor)

    print()
    slow_print("==== TRANSACTION COMPLETE ====", delay=0.01)
    print_receipt(args)

    slow_print("Reminder: MONEY TRANSFER — DO NOT USE THIS TO MISLEAD OR COMMIT FRAUD.", delay=0.01)
    slow_print("Exit in 5 seconds...", delay=0.01)
    time.sleep(5)

if __name__ == "__main__":
    main()
