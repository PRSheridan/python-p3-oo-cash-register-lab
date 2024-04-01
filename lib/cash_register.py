#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    for test in range(quantity):
      self.items.append(item)
    self.previous_transactions.append(
      {"item": item, "price": price, "quantity": quantity}
    )

  def apply_discount(self):
    if self.discount > 0:
      self.total = self.total - (self.total * (self.discount/100))
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
 
  def void_last_transaction(self):
    if self.previous_transactions == []:
      print("no previous transaction")
    else:
      self.total -= (self.previous_transactions[-1]["price"] * self.previous_transactions[-1]["quantity"])
