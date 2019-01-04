class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bn = bin(n)[2:]
        if len(bn) < 32:
            bn = '0'* (32-len(bn)) + bn
        return int(bn[::-1],2)
