"""
Simple hashmap using python arrays.
A couple improvements it could use:
    - store list of all keys for __repr__ printing
    - automatically resize
"""

class HashMap:
    def __init__(self, size=97):
        self.size = size
        self.data = [[] for _ in range(size)]

    def _hash_idx(self, key):
        return hash(key) % self.size

    def get(self, key):
        for k, v in self.data[self._hash_idx(key)]:
            if key == k:
                return v
        raise KeyError

    def set(self, key, value):
        data = self.data[self._hash_idx(key)]
        replaced = False
        for i in range(len(data)):
            if key == data[i][0]:
                replaced = True
                data[i] = (key, value)
                break
        if not replaced:
            data.append((key, value))

    def delete(self, key):
        data = self.data[self._hash_idx(key)]
        for i in range(len(data)):
            if data[i][0] == key:
                del data[i]
                return
        raise KeyError
        
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __delitem__(self, key):
        return self.delete(key)

if __name__ == '__main__':
    import unittest

    class HashMapTest(unittest.TestCase):
        def test_basics(self):
            m = HashMap()

            with self.assertRaises(KeyError):
                m['a']
            with self.assertRaises(KeyError):
                del m['a']
            with self.assertRaises(KeyError):
                del m['b']
                
            m['a'] = 42
            self.assertEqual(m['a'], 42)
            m['a'] = 44
            self.assertEqual(m['a'], 44)
            a = {'a': 234}
            m[34] = a
            self.assertEqual(m[34], a)

            del m['a']
            with self.assertRaises(KeyError):
                m['a']
            with self.assertRaises(KeyError):
                del m['a']

        def test_collisions(self):
            # 42 and 139 have the same hash_idx
            m = HashMap()
            self.assertEqual(m._hash_idx(42), m._hash_idx(139))
            m[42] = 'foo' 
            m[139] = 'bar'
            self.assertEqual(m[42], 'foo')
            self.assertEqual(m[139], 'bar')

            del m[139]
            self.assertEqual(m[42], 'foo')
            m[42] = 'foobar' 
            self.assertEqual(m[42], 'foobar')

    unittest.main()
