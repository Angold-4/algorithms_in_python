#  Angold4 20200627
import sys
data = []
for k in range(27):
    a = len(data)
    b = sys.getsizeof(data)
    print('length:', a, 'size in bytes:', b)
    data.append(None)

"""
length: 0 size in bytes: 56
length: 1 size in bytes: 88
length: 2 size in bytes: 88
length: 3 size in bytes: 88
length: 4 size in bytes: 88
length: 5 size in bytes: 120
length: 6 size in bytes: 120
length: 7 size in bytes: 120
length: 8 size in bytes: 120
length: 9 size in bytes: 184
length: 10 size in bytes: 184
length: 11 size in bytes: 184
length: 12 size in bytes: 184
length: 13 size in bytes: 184
length: 14 size in bytes: 184
length: 15 size in bytes: 184
length: 16 size in bytes: 184
length: 17 size in bytes: 256
length: 18 size in bytes: 256
length: 19 size in bytes: 256
length: 20 size in bytes: 256
length: 21 size in bytes: 256
length: 22 size in bytes: 256
length: 23 size in bytes: 256
length: 24 size in bytes: 256
length: 25 size in bytes: 256
length: 26 size in bytes: 336
"""
print()
print("---------------------------------")
print()

for k in range(27):
    a = len(data)
    b = sys.getsizeof(data)
    print('length:', a, 'size in bytes:', b)
    data.pop()

"""
('length:', 27, 'size in bytes:', 352)
('length:', 26, 'size in bytes:', 352)
('length:', 25, 'size in bytes:', 352)
('length:', 24, 'size in bytes:', 352)
('length:', 23, 'size in bytes:', 352)
('length:', 22, 'size in bytes:', 352)
('length:', 21, 'size in bytes:', 352)
('length:', 20, 'size in bytes:', 352)
('length:', 19, 'size in bytes:', 352)
('length:', 18, 'size in bytes:', 352)
('length:', 17, 'size in bytes:', 352)
('length:', 16, 'size in bytes:', 264)
('length:', 15, 'size in bytes:', 264)
('length:', 14, 'size in bytes:', 264)
('length:', 13, 'size in bytes:', 264)
('length:', 12, 'size in bytes:', 264)
('length:', 11, 'size in bytes:', 216)
('length:', 10, 'size in bytes:', 216)
('length:', 9, 'size in bytes:', 216)
('length:', 8, 'size in bytes:', 168)
('length:', 7, 'size in bytes:', 168)
('length:', 6, 'size in bytes:', 168)
('length:', 5, 'size in bytes:', 136)
('length:', 4, 'size in bytes:', 136)
('length:', 3, 'size in bytes:', 120)
('length:', 2, 'size in bytes:', 112)
('length:', 1, 'size in bytes:', 104)
"""
