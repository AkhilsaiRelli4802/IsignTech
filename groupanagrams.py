def groupanagrams(a):
    anagrams={}
    for i in a:
        sortedword = "".join(sorted(i))
        if sortedword in anagrams:
            anagrams[sortedword].append(i)
        else:
            anagrams[sortedword]=[i]
    return list(anagrams.values())
z=groupanagrams(["eat","tea","tan","ate","nat","bat"])
print(z)