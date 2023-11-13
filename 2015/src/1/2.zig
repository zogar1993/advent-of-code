const fs = @import("std").fs;
const heap = @import("std").heap;
const io = @import("std").io;
const fmt = @import("std").fmt;

pub fn run() !void {
    const path = "src/1/data.txt";
    var file = try fs.cwd().openFile(path, .{});
    defer file.close();

    var arena = heap.ArenaAllocator.init(heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    const read_buf = try file.readToEndAlloc(allocator, 1024 * 1024);
    defer allocator.free(read_buf);

    var floor: i32 = 0;
    var iteration: i32 = 0;
    for (read_buf) |character| {
        iteration += 1;
        if (character == '(') {
            floor += 1;
        } else {
            if (floor == 0)
                break;
            floor -= 1;
        }
    }

    const x = try fmt.allocPrint(allocator, "{d}\n", .{iteration});
    const stdout = io.getStdOut();
    _ = try stdout.writeAll(x);
}
