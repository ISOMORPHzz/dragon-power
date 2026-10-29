import unittest
from dragon_math import max_power
from dragon_dp import max_power_dp


class TestDragonPower(unittest.TestCase):

    def test_small_values(self):
        expected = {1: 1, 2: 2, 3: 3, 4: 4, 5: 6, 6: 9, 7: 12, 8: 18, 9: 27, 10: 36}
        for n, ans in expected.items():
            with self.subTest(n=n):
                self.assertEqual(max_power(n), ans)

    def test_math_equals_dp_all_range(self):
        for n in range(1, 100):
            with self.subTest(n=n):
                self.assertEqual(max_power(n), max_power_dp(n))

    def test_boundary_values(self):
        self.assertEqual(max_power(1), 1)
        self.assertEqual(max_power(99), 3 ** 33)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            max_power(0)
        with self.assertRaises(ValueError):
            max_power(100)

    def test_n7(self):
        # 7 = 3+2+2 → 3·2·2 = 12
        self.assertEqual(max_power(7), 12)


if __name__ == "__main__":
    unittest.main()
