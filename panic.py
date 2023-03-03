from cffi import FFI

cffi = FFI()
cffi.cdef(
    """
      void panic();
    """
)

import os

panic = cffi.dlopen(os.path.abspath("panic.dll"))

print(panic.panic())
