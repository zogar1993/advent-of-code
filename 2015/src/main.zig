const fs = @import("std").fs;
const heap = @import("std").heap;
const io = @import("std").io;
const std = @import("std");

pub fn main() !void {
    const path = "src/1/data.txt";
    var file = try fs.cwd().openFile(path, .{});
    defer file.close();

    var arena = heap.ArenaAllocator.init(heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    const read_buf = try file.readToEndAlloc(allocator, 1024 * 1024);
    defer allocator.free(read_buf);

    var floor: i32 = 0;
    for (read_buf) |character| {
        if (character == '(') {
            floor += 1;
        } else {
            floor -= 1;
        }
    }

    const x = try std.fmt.allocPrint(allocator, "{d}", .{floor});
    const stdout = io.getStdOut();
    _ = try stdout.writeAll(x);

    //// Prints to stderr (it's a shortcut based on `std.io.getStdErr()`)
    //std.debug.print("All your {s} are belong to us.\n", .{"codebase"});
    //
    //// stdout is for the actual output of your application, for example if you
    //// are implementing gzip, then only the compressed bytes should be sent to
    //// stdout, not any debugging messages.
    //const stdout_file = std.io.getStdOut().writer();
    //var bw = std.io.bufferedWriter(stdout_file);
    //const stdout = bw.writer();
    //
    //try stdout.print("Run `zig build test` to run the tests.\n", .{});
    //
    //try bw.flush(); // don't forget to flush!
}

test "simple test" {
    var list = std.ArrayList(i32).init(std.testing.allocator);
    defer list.deinit(); // try commenting this out and see if zig detects the memory leak!
    try list.append(42);
    try std.testing.expectEqual(@as(i32, 42), list.pop());
}
