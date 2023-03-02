from cffi import FFI

cffi = FFI()
cffi.cdef(
    """
      double sqrt(double x);
    """
)

import os

simple = cffi.dlopen(os.path.abspath("simple.dll"))

print(simple.sqrt(2))
