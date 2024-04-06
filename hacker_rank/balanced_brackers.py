def isBalanced(s):
    if len(s) % 2 != 0:  
        return 'NO'

    stack = []
    pair = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for char in s:
        if char in pair.values():
            stack.append(char)
        else:
            if not stack or stack.pop() != pair[char]:
                return 'NO'
    
    return 'YES'

if __name__ == '__main__':
    print(isBalanced('{[()]}'))
    print(isBalanced('{[(])}'))
    print(isBalanced('{{[[(())]]}}'))