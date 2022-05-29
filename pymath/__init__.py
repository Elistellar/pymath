from decimal import getcontext


__all__ = ['set_float_precision']

def set_float_precision(ndigit: int):
    """
    Set the precision of all Decimal numbers to 10^(-ndigit).
    """
    getcontext().prec = ndigit
