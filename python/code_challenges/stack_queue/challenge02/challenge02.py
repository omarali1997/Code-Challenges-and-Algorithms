# Write here the code challenge solution

class Valid_Parentheses():
    def isValid(self, s):
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0 # 3


if __name__ == '__main__':

    v=Valid_Parentheses()

    print(v.isValid('()')) # True
    print(v.isValid('{}')) # True
    print(v.isValid('()[]')) # True

    print(v.isValid('{)}')) # False
    print(v.isValid('{}[{]')) # False
    print(v.isValid('{}()')) # False
    print(v.isValid('{}(){[]')) # False
    print(v.isValid('()')) # False
    print(v.isValid('()[]')) # False
    print(v.isValid('()()')) # False
 