
my_words = ['chair', 'racket', 'tumeric', 'touch', 'height']

def can_cycle(words):
    table = [0] * 26
    
    for w in words:
        table[ord(w[0]) - 97] += 1
        table[ord(w[-1]) - 97] -= 1

    return all([i - 1 for i in table if i > 0])


if __name__ == '__main__':
    print(can_cycle(my_words))

