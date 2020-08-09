class Solution:
    def compress(self, chars):
        index = i = 0
        length = len(chars)

        while i < length:
            j = i + 1
            while j < length and chars[i] == chars[j]:
                j += 1
            num = j - i
            chars[index] = chars[i]
            index += 1
            if num > 1:
                num_s = str(num)
                for k, n in enumerate(num_s, index):
                    chars[k] = n
                index = k + 1

            i = j

        return index
