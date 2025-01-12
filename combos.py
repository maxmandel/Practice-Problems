import itertools

def find_combinations(target_sum):
    result = []
    for combination in itertools.product(range(97, 126), repeat=6):
        if sum(combination) == target_sum:
            result.append(''.join(map(chr, combination)))
    return result

target_sum = 654
combinations = find_combinations(target_sum)

for combo in combinations:
    if combo[0] == "H":
        print(combo)
