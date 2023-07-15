def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    conversion_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, \
    "M":1000}
    num_lst = []
    for i in range(len(s)):
        num_lst.append(conversion_dict[s[i]])
    copy_nl = num_lst[:]
    counter = 0
    for j in range(len(copy_nl) - 1):
        ## consider j, j+1
        if copy_nl[j+1] > copy_nl[j]:
            num_lst[j - counter] = num_lst[j+1 - counter] - num_lst[j - counter]
            del num_lst[j+1 - counter]
            counter += 1

    return sum(num_lst)