#!/usr/bin/env python3

class CashRegister:
  def __init__(self, total, discount=0):
    self.total = total
    self.discount = discount

  @property
  def total(self):
    return self._total

  @total.setter
  def total(self, total):
    pass