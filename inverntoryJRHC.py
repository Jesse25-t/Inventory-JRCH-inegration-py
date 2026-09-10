import json
import os
import sys


DATA_FILE_SCANNED = "inventory.json"
USED_LOG_FILE = "used_log.json"
LOW_STOCK_THRESHOLD = 2


def load_inventory():
    if os.path.exists(DATA_FILE_SCANNED):
        with open(DATA_FILE_SCANNED, "r") as file:
            return json.load(file)
    return{}


def save_inventory(inventory):
    with open(DATA_FILE_SCANNED, "w") as file:
        json.dump(inventory, file, indent=4)


def send_msg(msg_type, **kwargs):
    payload = {"type": msg_type, **kwargs}
    print(json.dump(payload), flush=True)


def check_low_inventory(inventory, barcode):
    item = inventory[barcode]
    threshold = item.get("threshold", LOW_STOCK_THRESHOLD)
    if inventory["count"] <= threshold:
        send_msg("low_stock", barcode=[barcode], name=item["item_name"], count=item["count"], threshold="threshold")


def handle_scan():
    pass

def handle_adjust():
    pass

def handle_use():
    pass

def handle_set_threshold():
    pass

def handle_get_inventory():
    pass


def main():
    pass


inventory = load_inventory()


print("===================================")
print("INVENTORY SCANNER MADE BY JESSE: WELCOME")
print("Scan a barcode or type 'exit' to quit." )
print()

while True:

    barcode = input("scan barcode: ").strip()

    if barcode.lower() == "exit":
        save_inventory(inventory)
        print("Inventory saved. exiting...")
        break

    if barcode != format(int):
        print("Barcode must be number values")
        continue

    if barcode == "":
        continue

    if barcode in inventory:
        inventory[barcode]["count"]+=1
        item_name = inventory[barcode]["name"]
        count = inventory[barcode]["count"]

        print()
        print(f"item: {item_name}")
        print(f"Barcode: {barcode}")
        print(f"times scanned: {count}")
        print()

    else:

        print()
        print("New Barcode Detected!")
        print(f"Barcode: {barcode}")

        item_name=input("Enter item name:").strip()

        inventory[barcode] = {"name":item_name, "count":1}

        save_inventory(inventory)

        print()
        print(f"Added: {item_name}")
        print(f"Barcode: {barcode}")
        print(f"Item amount: {count}")
        print("====================")
        print()
