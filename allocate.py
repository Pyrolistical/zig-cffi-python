from cffi import FFI

cffi = FFI()
cffi.cdef(
    """
      char* allocByteArrayZ(long long size);
      void printZ(char* messageZ);
      void freeByteArrayZ(char* array);
      bool detectLeaks();
    """
)

import os

allocate = cffi.dlopen(os.path.abspath("allocate.dll"))

messageZ = allocate.allocByteArrayZ(5)
messageZ[0:5] = b"hello"

allocate.printZ(messageZ)

allocate.freeByteArrayZ(messageZ)

print("leaked: {leaked}".format(leaked=allocate.detectLeaks()))
