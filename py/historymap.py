import hashlib

class HistoryMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key, value, time):
        _key = hashlib.md5((str(key) + str(time)).encode()).hexdigest()
        self.hmap[_key] = value
    
    def get(self, key, time):
         _key = hashlib.md5((str(key) + str(time)).encode()).hexdigest()
         return self.hmap[_key]

    def __repr__(self):
        return str(self.hmap)



h = HistoryMap()

h.set('harry', 100, 0)
h.set('bri', 200, 1)
h.set('harry', 200, 1)

print(h.get('harry', 1))
