import unittest
from player import Dealer


class TestBlackJack(unittest.TestCase):

    def test_dealer_hit_or_stand(self):
        dealer = Dealer()
        self.assertEqual(dealer.hit_or_stand([1, 11, 21]), "S")
        self.assertEqual(dealer.hit_or_stand([7, 17, 27]), "H")
        self.assertEqual(dealer.hit_or_stand([17, 27]), "S")
        self.assertEqual(dealer.hit_or_stand([8, 18, 28]), "S")


if __name__ == "__main__":
    unittest.main()
