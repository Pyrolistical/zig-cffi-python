const std = @import("std");

const SomeStruct = extern struct {
    boolean: bool,
    byte: u8,
    array: [6]u8,
    stringZ: [*:0]const u8,
};

export fn getStruct() callconv(.C) SomeStruct {
    return .{
        .boolean = true,
        .byte = 42,
        .array = .{ 5, 4, 3, 2, 1, 0 },
        .stringZ = "hello from zig",
    };
}

export fn setStruct(some_struct: SomeStruct) callconv(.C) void {
    std.debug.print("{}\n", .{some_struct});
    std.debug.print("{s}\n", .{some_struct.stringZ});
}
