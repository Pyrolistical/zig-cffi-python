const std = @import("std");

// messageZ must be null-terminated
export fn printZ(messageZ: [*]u8) void {
    // [*:0]u8 is not allowed by C ABI, cast to right type
    const message = @ptrCast([*:0]u8, messageZ);

    std.debug.print("{s}\n", .{message});
}
