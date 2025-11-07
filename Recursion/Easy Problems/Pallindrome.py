def pallindrome(s):

    res =  helper(s, 0, len(s) - 1)
    if res:
        print("true")
    else:
        print("false")

def helper(s, left, right):
    if left>=right:
        return True
    
    if  s[left] != s[right]:
        return False

    return helper(s, left+1,right-1)


pallindrome('aaba')

