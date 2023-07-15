"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    opener_dict = {'(':')', '[':']', '{':'}'}
    closer_dict = {')':'(', ']':'[', '}':'{'}
    s = list(s)
    s_copy = s[:]
    for i in range(len(s)):
        if s[i] in closer_dict.keys() and i == 0:
            return False
        elif s[i] in opener_dict.keys():
            if opener_dict[s[i]] not in s[i+1:]:
                return False
            s_copy.remove(s[i])
            s_copy.remove(opener_dict[s[i]])
    if len(s_copy) > 0:
        return False
    return True