"""
Simple set based on my hashmap.
Could use things like pop(), intersection(), etc.
"""

from hashmap import HashMap

class SimpleSet(HashMap):
    def add(self, key):
        return self.set(key, None)

    def remove(self, key):
        return self.delete(key)

    def contains(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False


if __name__ == '__main__':
    import unittest

    class SimpleSetTest(unittest.TestCase):
        def test_set(self):
            s = SimpleSet()
            self.assertFalse(s.contains(42))

            s.add(42)
            s.add('foo')
            self.assertTrue(s.contains(42))
            self.assertTrue(s.contains('foo'))

            s.remove('foo')
            self.assertTrue(s.contains(42))
            self.assertFalse(s.contains('foo'))

    unittest.main()
