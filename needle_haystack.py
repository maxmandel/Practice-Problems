def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # make every letter in needle unique
    needle = list(needle)
    seen = []
    times_called = {}
    for idx, letter in enumerate(needle):
        if letter not in seen:
            seen.append(letter)
            times_called[letter] = 1
        else:
            times_called[letter] += 1
            needle[idx] = letter + str(times_called[letter])

    # record at which indices in haystack needle letters appear
    track_appearances = {} # needle letters correspond to haystack indices
    for letter in needle:
        track_appearances[letter] = []
    for i in range(len(needle)):
        if needle[i][0] not in haystack:
            return -1 # short circuit if a necessary letter doesn't appear at all
        for j in range(len(haystack)):
            if haystack[j] == needle[i][0]:
                track_appearances[needle[i]].append(j)

    live_combos = []
    # here track_appearances dict should be filled for each letter in needle
    for idx_lst in track_appearances.values():
        if track_appearances[needle[0]] == idx_lst: # if we're on the first idx lst
            for idx in idx_lst:
                live_combos.append(idx) # every appearance of the first letter
                                        # is a possible starting point of needle
        else:
            live_combos_copy = live_combos[:]
            for idx in live_combos:
                live_combos_copy.remove(idx)
                if (idx + 1) in idx_lst: # if the next index appears as a location
                                            # of the next letter in needle
                    live_combos_copy.append(idx + 1) # combo remains live
            live_combos = live_combos_copy[:]
    live_combos = live_combos_copy
    final_combos = []
    for idx in live_combos:
        if (idx + 1) in track_appearances[needle[-1]]:
            final_combos.append(idx + 1)
    # evaluate
    if len(final_combos) == 0:
        return - 1
    else:
        best_end = min(live_combos)
        first_occurrence = best_end + 1 - len(needle)
    return first_occurrence

##TEST
num = strStr("neatochpsychicphanochic", "chic")