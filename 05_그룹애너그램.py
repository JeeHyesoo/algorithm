# 문자열 배열을 받아 애너그램 단위로 그룹핑하라

from typing import Collection
import collections

strs = ['eat','tea','tan','ate','nat','bat']

def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    
    return list(anagrams.values())

print(groupAnagrams(strs))