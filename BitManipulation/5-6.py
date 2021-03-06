"""
Write a program to swap odd and even bits in an integer with as few instructions as
possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, etc).
"""

"""
solution: Mask all odd bits with 10101010 in binary (which is 0xAA), 
then shift them left to put them in the even bits. 
Then, perform a similar operation for even bits. 
This takes a total 5 instructions
"""

ODD_INT_MASK = 0xAAAAAAAA
EVEN_INT_MASK = 0x55555555
def swapOddEvenBits(x):
    return ((x & ODD_INT_MASK) >> 1) | ((x & EVEN_INT_MASK) << 1)

test = 12345
print bin(test)
print bin(swapOddEvenBits(test))

