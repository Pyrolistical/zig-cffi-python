# zig cffi python examples

Demonstrates passing data back and forth between [Zig](https://ziglang.org/) and [Python](https://www.python.org/) via [cffi](https://cffi.readthedocs.io/en/latest/).

Each example is standalone and consist a single .zig and .py file.

## How to run examples

1. Build the example as a library

```sh
zig build-lib -dynamic [example].zig
```

2. Run the python script

```sh
python [example].py
```

## Requirements

- Zig 11+
- Python 3+
