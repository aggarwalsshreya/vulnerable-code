_transactions = {}


def transfer(account_from, account_to, amount):
    if _transactions.get(account_from, 0) >= amount:
        balance = _transactions.get(account_from, 0)
        _transactions[account_from] = balance - amount  # CWE-362 race without lock
        _transactions[account_to] = _transactions.get(account_to, 0) + amount
        return True
    return False


def get_discount(customer):
    return customer.profile.plan.discount_percent  # CWE-476 if profile or plan is None


def item_at(items, index):
    return items[int(index)]  # CWE-125/CWE-129 analog
