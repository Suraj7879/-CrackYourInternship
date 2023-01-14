# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s):
        def precedence(c):
            return c == '*' or c == '/'

        op, num, cur = deque(), deque(), 0
        for c in s + '#':
            if c == ' ': continue
            elif c.isdigit():
                cur = cur * 10 + int(c)
            else:
                num.append(cur)
                while op and precedence(c) <= precedence(op[-1]):
                    num1, num2, curOp = num.pop(), num.pop(), op.pop()
                    if   curOp == '*': num.append(num2 * num1)
                    elif curOp == '/': num.append(num2 // num1)
                    elif curOp == '+': num.append(num2 + num1)
                    elif curOp == '-': num.append(num2 - num1)
                op.append(c)
                cur = 0
    
        return num.pop()
