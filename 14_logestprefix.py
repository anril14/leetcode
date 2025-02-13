from typing import List

class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        strs.sort(key= lambda x: len(x))
        comb = ""
        counter = -1
        break_state = False
        if strs[0]:
            for l in strs[0]:
                counter+=1
                for j in range(len(strs)):
                    if str(l) != str(strs[j][counter]):
                        break_state=True
                        break
                if break_state:
                    break
                else:
                    comb += str(l)
        return comb

solution = Solution()
print(solution.longest_common_prefix(["flower","flow","flight"]))
