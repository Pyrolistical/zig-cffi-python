from cffi import FFI

cffi = FFI()
cffi.cdef(
    """
      void printZ(char* message);
    """
)

import os

hello_world = cffi.dlopen(os.path.abspath("hello-world.dll"))

# pass in null-terminated array
hello_world.printZ(b"Hello world\x00")
