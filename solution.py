import zlib

def solve(value):
    return format(zlib.crc32(value.encode('utf-8')), '08x')
