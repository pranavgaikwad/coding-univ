import unittest


class MergeSort:
    def merge(self, a, b):
        alen = len(a)
        blen = len(b)

        if not a:
            return b

        if not b:
            return a

        if a[0] < b[0]:
            return [a[0]] + self.merge(a[1:], b)
        else:
            return [b[0]] + self.merge(a, b[1:])

    def sort(self, a):
        right = len(a)
        mid   = right / 2

        if right == 0:
            return a

        if right == 1:
            return a

        return self.merge(self.sort(a[0:mid]), self.sort(a[mid:]))

class MergeSortTest(unittest.TestCase):
    def test_sort(self):
        a = [10, 9, 8, 7, 6]
        exp = [6, 7, 8, 9, 10]
        self.assert_sort(a, exp)

        a = [-1, -23, 0, 87, 99, 23, 4, 102]
        exp = [-23, -1, 0, 4, 23, 87, 99, 102]
        self.assert_sort(a, exp)

        a = []
        exp = []
        self.assert_sort(a, exp)

        a = [2]
        exp = [2]
        self.assert_sort(a, exp)

    def test_merge(self):
        a = [1, 2, 5]
        b = [3, 4, 8]

        exp = [1, 2, 3, 4, 5, 8]
        self.assert_merge(a, b, exp)

        b = []
        exp = a
        self.assert_merge(a, b, exp)

        b = [1, 2, 5]
        exp = [1, 1, 2, 2, 5, 5]
        self.assert_merge(a, b, exp)

        a = [0, 2, 8]
        b = [1, 2, 5]
        exp = [0, 1, 2, 2, 5, 8]
        self.assert_merge(a, b, exp)

    def assert_merge(self, a, b, exp):
        act = MergeSort().merge(a, b)
        self.assertEqual(act, exp)

    def assert_sort(self, a, exp):
        act = MergeSort().sort(a)
        self.assertEqual(act, exp)


if __name__ == "__main__":
    unittest.main()