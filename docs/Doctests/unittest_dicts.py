import unittest

class TestDictionaries(unittest.TestCase):
    def test_dict_contains_subset(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        subset = {'a': 1, 'b': 2}
        self.assertDictContainsSubset(subset, dict1)

    def test_dict_equal(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'a': 1, 'b': 2, 'c': 3}
        self.assertDictEqual(dict1, dict2)

    def test_item_in_dict(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        self.assertIn('a', dict1)
        self.assertIn(2, dict1.values())

if __name__ == '__main__':
    unittest.main()
