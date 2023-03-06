from cffi import FFI

cffi = FFI()
cffi.cdef(
    """
      char* allocByteArrayZ(unsigned long long size);
      void printZ(char* message);
      void freeByteArrayZ(char* array);
      bool detectLeaks();
    """
)

import os

allocate = cffi.dlopen(os.path.abspath("allocate.dll"))

message = allocate.allocByteArrayZ(5)
message[0:5] = b"hello"

allocate.printZ(message)

allocate.freeByteArrayZ(message)

print("leaked: {leaked}".format(leaked=allocate.detectLeaks()))
