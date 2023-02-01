from enum import Enum


# defining a class with an argument - defines which class it inherits from
class TransactionType(Enum):
    # create 2 "types" for the new enumerator
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
