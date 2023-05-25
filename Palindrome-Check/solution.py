def isPalindrome(string):
    left, right = 0, len(string)-1
    while left<right:
        if string[left] != string[right]:
            return False
        left, right = left+1, right-1
    return True