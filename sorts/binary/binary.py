import unittest


class Binary:
    def binary(self, a, left, right, val):
        mid = left + (right - left) / 2

        if right >= left:
            if a[mid] == val:
                return mid 
        
            if a[mid] > val:
                return self.binary(a, left, mid-1, val)
            elif a[mid] < val:
                return self.binary(a, mid+1, right, val)
    
        return -1

    def find_el(self, a, val):
        right = len(a) - 1
        left  = 0
    
        return self.binary(a, left, right, val)

class BinaryTest(unittest.TestCase):
    def test_find_el(self):
        a = [0, 2, 3, 29, 40, 63, 79, 86, 88, 105, 132, 171, 219]

        val = 171
        exp = 11
        self.assert_binary(a, val, exp)

        val = 80
        exp = -1
        self.assert_binary(a, val, exp)

        val = 132
        exp = 10
        self.assert_binary(a, val, exp)

        val = 0
        exp = 0
        self.assert_binary(a, val, exp)

        a = []
        val = 132
        exp = -1
        self.assert_binary(a, val, exp)

        a = [2, 0]
        val = 132
        exp = -1
        self.assert_binary(a, val, exp)

    def assert_binary(self, a, val, exp):
        act = Binary().find_el(a, val)
        self.assertEqual(act, exp)


if __name__ == "__main__":
    unittest.main()