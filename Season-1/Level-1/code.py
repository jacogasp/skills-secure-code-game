'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')


MAX_PAYMENT_AMOUNT = 1e5
MIN_PAYMENT_AMOUNT = -MAX_PAYMENT_AMOUNT
MAX_ITEM_AMOUNT = 2e4
MIN_ITEM_AMOUNT = 0
MAX_ITEM_QUANTITY = 100
MIN_ITEM_QUANTITY = 0
MAX_TOTAL_AMOUNT = 1e4
MIN_TOTAL_AMOUNT = -MAX_TOTAL_AMOUNT

def validorder(order: Order):
    net = 0
    for item in order.items:
   
        if item.type == 'payment':
            if MIN_PAYMENT_AMOUNT < item.amount < MAX_PAYMENT_AMOUNT:
                net += item.amount
            else:
                print("Payment not valid: %s" % item.amount)
                continue
        elif item.type == 'product':
            if not MIN_ITEM_QUANTITY <= item.quantity <= MAX_ITEM_QUANTITY:
                print("Item quantity not valid: %s" % item.quantity)
                continue
            if not MIN_ITEM_AMOUNT < item.amount < MAX_ITEM_AMOUNT:
                print("Item amount not valid: %s" % item.amount)
                continue
            net -= item.amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type
    if not MIN_TOTAL_AMOUNT < net < MAX_TOTAL_AMOUNT:
        return "Total amount payable for an order exceeded"
    if abs(net) >= 0.01:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id