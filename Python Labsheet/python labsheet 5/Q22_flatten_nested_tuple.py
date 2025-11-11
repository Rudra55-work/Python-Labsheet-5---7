import itertools
t=(1,(2,3),(4,5))
print(tuple(itertools.chain.from_iterable([x if isinstance(x, tuple) else (x,) for x in t])))