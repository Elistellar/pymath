# Pymath Package

Pymath is a python package adding some math objects such as lines, segments or polygons.
It's still under developpement and will be updated slowly.

This lib uses the `Decimal` object (that you can import from the native decimal module) instead of basic int or float to avoid division errors.

## Install

This lib is still under development so you can install it using :
```
pip install https://github.com/Elistellar/pymath/raw/master/dist/pymath-0.0.1.tar.gz
```

## Exemple
This is a short example about how calculate the intersection of 2 lines.
```python
from decimal import Decimal
from pymath.geometry.d2 import Point, Line

A = Point(Decimal(0), Decimal(0))
B = Point(Decimal(3), Decimal(3))
C = Point(Decimal(1), Decimal(2))
D = Point(Decimal(2), Decimal(1))

l1 = Line(A, B)
l2 = Line(C, D)

print(l1.intersect(l2))
print(l1.get_intersection(l2))
```

```
>>> True
>>> Point(1.5, 1.5)
```