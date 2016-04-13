import struct

b = struct.pack('>I', 10240099)
print(b)

i = struct.unpack('>I', b)
print(i)

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
r = struct.unpack('<ccIIIIIIHH', s)
print(r)