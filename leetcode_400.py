class Solution:
    def findNthDigit(self, n: int) -> int:
        wei = 1
        sum_w = wei * 9 * 10 ** (wei - 1)
        while n >= sum_w:
            sum_w += wei * 9 * 10 ** (wei - 1)
        sum_w -= wei * 9 * 10 ** (wei - 1)
        n -= sum_w
        pos = n % wei
        n //= wei
        if pos == 0:
            n += 10**(wei - 1) - 1
            return int(str(n)[-1])
        else:
            n += 10**(wei - 1)
            return int(str(n)[pos - 1])