# ფუნქცია ამოწმებს მარტივია თუ არა რიცხვი. (მარტივია თუ მხოლოდ 1_ზე და საკუთარ თავზე იყოფა)
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# გატესტე ფუნქცია'unittest'_ის დახმარებით.
import unittest


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        # Test prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

        # Test non-prime numbers
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))


if __name__ == "__main__":
    unittest.main()
