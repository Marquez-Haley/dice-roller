import unittest
from dice import Dice

class TestDiceRoller(unittest.TestCase):
    six_dice = Dice(6)
    uneven_dice = Dice(5)

    def test_new_dice(self):
        new_dice = Dice(6)
        self.assertEqual(new_dice.sides, self.six_dice.sides)
        self.assertEqual(new_dice.sides, 6)

    def test_uneven_dice(self):
        self.assertIsNone(self.uneven_dice.sides)
        self.assertEqual(self.uneven_dice.total, 0)

    def test_roll(self):
        new_dice = Dice(6)
        self.six_dice.roll()
        self.assertNotEqual(self.six_dice.total, new_dice.total)

    def test_uneven_dice_roll(self):
        self.assertEqual(self.uneven_dice.total, 0)
        self.assertEqual(self.uneven_dice.roll(), 0)
        
    def test_total(self):
        self.six_dice.total = 4
        temp_total = self.six_dice.get_total()
        self.assertTrue(self.six_dice.get_total())
        self.assertEqual(self.six_dice.total, temp_total)

    def test_clear(self):
        self.assertIsNone(self.six_dice.clear())
        self.assertEqual(self.six_dice.total, 0)

if __name__ == '__main__':
    unittest.main()