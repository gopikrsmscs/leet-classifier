class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #lct:stack,string;
        #lcd:E_1;
        stack_s = []
        stack_t = []
        for char in s:
            if char == '#':
                if len(stack_s) == 0:
                    continue
                else:
                    stack_s.pop()
            else:
                stack_s.append(char)
        for char in t:
            if char == '#':
                if len(stack_t) == 0:
                    continue
                else:
                    stack_t.pop()
            else:
                stack_t.append(char)
        return True if stack_t == stack_s else False
        

