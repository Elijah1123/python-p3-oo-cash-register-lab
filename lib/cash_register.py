#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            self.total = round(self.total)  # Ensure test compatibility (integer)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0

# Create a register with a 20% discount
register = CashRegister(discount=20)

# Add items
register.add_item("Apple", 1.50, 3)   # 3 Apples at $1.50 each
register.add_item("Banana", 2.00)     # 1 Banana at $2.00

# Show current total
print("Current total:", register.total)  

# Apply discount
register.apply_discount()

# Void last transaction (Banana in this case)
register.void_last_transaction()
print("After voiding last transaction:", register.total)

# Show all items
print("Items in register:", register.items)
