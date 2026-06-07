class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in close_to_open.values():
                stack.append(c)
            else:
                if stack == []:
                    return False
                p = stack.pop()
                if p != close_to_open[c]:
                    return False
        
        if stack == []:
            return True
        else:
            return False