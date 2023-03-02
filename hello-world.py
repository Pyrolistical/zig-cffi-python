from cffi import FFI

cffi = FFI()
cffi.cdef(
    """
      void print(char* x);
    """
)

import os

helloWorld = cffi.dlopen(os.path.abspath("hello-world.dll"))

# pass in null-terminated array
helloWorld.print(b"Hello world\x00")
