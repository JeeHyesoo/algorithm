"""
금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력
"""
import re
import collections

paragraph = "hit hit a ball, bob bob Bob."
banned = "a"

def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]',' ', paragraph)
        .lower().split()
            if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

print(mostCommonWord(paragraph,banned))