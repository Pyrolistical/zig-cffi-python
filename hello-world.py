from cffi import FFI

cffi = FFI()
cffi.cdef(
    """
      void printZ(char* messageZ);
    """
)

import os

helloWorld = cffi.dlopen(os.path.abspath("hello-world.dll"))

# pass in null-terminated array
helloWorld.printZ(b"Hello world\x00")
