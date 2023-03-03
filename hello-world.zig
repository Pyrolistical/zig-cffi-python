const std = @import("std");

// messageZ must be null-terminated
export fn printZ(message: [*:0]u8) callconv(.C) void {
    std.debug.print("{s}\n", .{message});
}
