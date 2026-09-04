import json
import os

DATA_FILE_SCANNED = "inventory.json"


def load_inventory():
    if os.path.exists(DATA_FILE_SCANNED):
        with open(DATA_FILE_SCANNED, "r") as file:
            return json.load(file)
    return{}


def save_inventory(inventory):
    with open(DATA_FILE_SCANNED, "w") as file:
        json.dump(inventory, file, indent=4)


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
        gbreak

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
