from cffi import FFI

cffi = FFI()
cffi.cdef(
    """
      typedef struct {
        bool boolean;
        char byte;
        char array[6];
        char* stringZ;
      } SomeStruct;

      SomeStruct getStruct();
      void setStruct(SomeStruct some_struct);
    """
)

import os

struct_dict = cffi.dlopen(os.path.abspath("struct-dict.dll"))


def toDict(struct):
    return dict(
        boolean=struct.boolean,
        byte=struct.byte[0],
        array=list(cffi.buffer(struct.array)[:]),
        stringZ=cffi.string(struct.stringZ).decode("utf-8"),
    )


print(toDict(struct_dict.getStruct()))


def toStruct(some_dict):
    some_struct = cffi.new("SomeStruct *")
    some_struct.boolean = some_dict["boolean"]
    some_struct.byte = some_dict["byte"].to_bytes(length=1, byteorder="big")
    some_struct.array = cffi.from_buffer("char[6]", bytearray(some_dict["array"]))
    some_struct.stringZ = cffi.from_buffer(
        "char[]", some_dict["stringZ"].encode("utf-8")
    )

    # note some_struct remains alive due to some_struct[0]
    # see https://cffi.readthedocs.io/en/latest/ref.html#ffi-new
    return some_struct[0]


struct_dict.setStruct(
    toStruct(
        dict(
            boolean=True,
            byte=42,
            array=[5, 4, 3, 2, 1, 0],
            stringZ="hello from python",
        )
    )
)
