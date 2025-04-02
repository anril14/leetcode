class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        print(i, j)
        while i != j and i < j:
            if s[i] in vowels and s[j] in vowels:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i += 1
                j -= 1
                continue
            if s[i] in vowels:
                j -= 1
                continue
            if s[j] in vowels:
                i += 1
                continue
            i += 1
            j -= 1
        s = ''.join(s)
        return s


solution = Solution()
print(solution.reverseVowels('IceCreAm'))
