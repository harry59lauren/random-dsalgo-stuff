
def findAndReplacePattern(words, pattern):
    return [ word for word in words if matches_pattern(word, pattern) ]

def matches_pattern(word, pattern):
    pattern_mapping = dict()
    if len(word) != len(pattern):
        return False

    for c1, c2 in zip(pattern, word):
        if c1 in pattern_mapping.keys() or c2 in pattern_mapping.keys():
            if pattern_mapping[c1] != c2 or pattern_mapping[c2] != c1:
                return False
            else:
                pattern_mapping[c1] = c2
                pattern_mapping[c2] = c1
          
    print(pattern_mapping)
    return True


print(findAndReplacePattern(["xx"], 'ba'))