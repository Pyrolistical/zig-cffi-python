const std = @import("std");
var gpa = std.heap.GeneralPurposeAllocator(.{}){};

export fn allocByteArrayZ(size: u64) [*:0]u8 {
    const arrayZ = gpa.allocator().allocSentinel(u8, size, 0) catch unreachable;
    return arrayZ.ptr;
}

export fn printZ(message: [*:0]u8) callconv(.C) void {
    std.debug.print("{s}\n", .{message});
}

export fn freeByteArrayZ(array: [*:0]u8) callconv(.C) void {
    const len = std.mem.len(array);
    gpa.allocator().free(array[0..len]);
}

export fn detectLeaks() bool {
    return gpa.detectLeaks();
}
