import builtins
import types
from random import randint

# Get all built-in functions (as function objects)
builtin_funcs = [getattr(builtins, name) for name in dir(builtins)
                 if isinstance(getattr(builtins, name), types.BuiltinFunctionType)]

# Example: print first 5
print(len(builtin_funcs))

while builtin_funcs:
    a, b = randint(0, len(builtin_funcs)-1), randint(0, len(builtin_funcs)-1)
    if a == b:
        continue
    aa, bb = builtin_funcs.pop(a), builtin_funcs.pop(b)
    aa = bb

print('done!')
