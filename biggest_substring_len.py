def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    # Short-circuit trivial cases
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    
    substrings = []
    seenin_curr = []
    curr = ""
    i = 0
    count_resets = 0

    while i < len(s):
        if s[i] not in seenin_curr:
            curr += s[i]
            seenin_curr.append(s[i])
            if i == len(s) - 1:
                substrings.append(curr)
        else:
            count_resets += 1
            substrings.append(curr)
            seenin_curr = []
            curr = ""
            i = count_resets - 1
        
        i += 1
    
    substring_lengths = []
    for st in substrings:
        substring_lengths.append(len(st))
    
    return max(substring_lengths)
    

