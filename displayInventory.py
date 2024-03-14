stuff = {"rope": 1, "torch": 6, "gold coin": 42, "ring": 1, "apple": 12}


def displayInventory(inventory):
    # your code goes here
    total = 0
    print("Inventory:")

    for k, v in inventory.items():
        print(v, k)
        total += v

    print("Total number of items:", total)


if __name__ == "__main__":
    displayInventory(stuff)
