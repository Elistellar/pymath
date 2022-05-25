from decimal import getcontext


def set_float_precision(ndigit: int):
    getcontext().prec = ndigit
