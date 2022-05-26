from decimal import getcontext


__all__ = ['set_float_precision']

def set_float_precision(ndigit: int):
    getcontext().prec = ndigit
