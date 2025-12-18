import unittest
from coins_task import find_coins_greedy, find_min_coins


class TestCoinChange(unittest.TestCase):

    def test_greedy_standard_case(self):
        result = find_coins_greedy(113)
        expected = {50: 2, 10: 1, 2: 1, 1: 1}
        self.assertEqual(result, expected)

    def test_dp_standard_case(self):
        result = find_min_coins(113)
        expected = {50: 2, 10: 1, 2: 1, 1: 1}
        self.assertEqual(result, expected)

    def test_zero_amount(self):
        self.assertEqual(find_coins_greedy(0), {})
        self.assertEqual(find_min_coins(0), {})

    def test_single_coin_match(self):
        self.assertEqual(find_coins_greedy(25), {25: 1})
        self.assertEqual(find_min_coins(25), {25: 1})

    def test_large_sum_correctness(self):
        target = 524
        res_greedy = find_coins_greedy(target)
        res_dp = find_min_coins(target)

        sum_greedy = sum(k * v for k, v in res_greedy.items())
        sum_dp = sum(k * v for k, v in res_dp.items())

        self.assertEqual(sum_greedy, target)
        self.assertEqual(sum_dp, target)


if __name__ == '__main__':
    unittest.main()
