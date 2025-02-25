class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        new_stack = []
        result = False

        for i, item in enumerate(s):
            # print(new_stack)
            if item == '[' or item == '(' or item == '{':
                # print(i, item)
                new_stack.append(item)
            else:
                if len(new_stack)==0:
                    result = False
                    break
                # print(i, item, new_stack[len(new_stack)-1])
                if item == ']' and new_stack[len(new_stack)-1]!='[':
                    break
                elif item == ')' and new_stack[len(new_stack)-1]!='(':
                    break
                elif item == '}' and new_stack[len(new_stack)-1]!='{':
                    break
                new_stack.pop()
                result = True
        if len(new_stack)>0:
            result = False
        return result

solution = Solution()
print(solution.isValid("()[]{}"))
print(solution.isValid("([])"))
print(solution.isValid("()"))
print(solution.isValid("["))
print(solution.isValid("]"))
print(solution.isValid("[[[]]"))
