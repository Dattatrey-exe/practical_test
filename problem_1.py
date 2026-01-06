from bisect import bisect_left

def successfulPairs(spells, potions, success):
    potions.sort()
    m = len(potions)
    res = []

    for spell in spells:
        # minimum potion strength required to reach 'success'
        required = (success + spell - 1) // spell  # equivalent to ceil(success/spell)
        
        # find the first index in potions where potion >= required
        idx = bisect_left(potions, required)
        # number of successful potions for this spell
        res.append(m - idx)

    return res

spells = [5,1,3]
potions = [1,2,3,7,5]
success = 8
print(successfulPairs(spells, potions, success))



print("Hellow World")