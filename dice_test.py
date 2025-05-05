import unittest
from dice import Dice
from unittest.mock import patch

class TestDiceRoller(unittest.TestCase):

    def setUp(self):
        self.six_dice = Dice(6)
        self.uneven_dice = Dice(5)

    def test_new_dice(self):
        new_dice = Dice(6)
        self.assertEqual(new_dice.sides, self.six_dice.sides)
        self.assertEqual(new_dice.sides, 6)

    def test_uneven_dice(self):
        self.assertIsNone(self.uneven_dice.sides)
        self.assertEqual(self.uneven_dice.total, 0)

    @patch('dice.random.randint', return_value = 4)
    def test_roll(self, mock_randint):
        dice = Dice(6)
        number = dice.roll()
        self.assertEqual(number, 4)
        self.assertEqual(dice.total, 4)

    def test_uneven_dice_roll(self):
        self.assertEqual(self.uneven_dice.roll(), 0)

    def test_total(self):
        self.six_dice.total = 4
        temp_total = self.six_dice.get_total()
        self.assertEqual(self.six_dice.get_total(), temp_total)

    def test_clear(self):
        self.assertIsNone(self.six_dice.clear())
        self.assertEqual(self.six_dice.total, 0)

    ##integration test ----
    def test_valid_rolls(self):
        dice = Dice(6)
        rolls = []
        for i in range(5):
            number = dice.roll()
            rolls.append(number)
            self.assertTrue(1 <= number <= 6)
        self.assertEqual(dice.get_total(), sum(rolls))
    
    def test_clearing_multiple_rolls(self):
        self.six_dice.roll()
        self.six_dice.roll()
        self.assertGreater(self.six_dice.get_total(), 0)
        self.six_dice.clear()
        self.assertEqual(self.six_dice.get_total(), 0)

    def test_invalid_rolls(self):
        dice = Dice(7)
        rolls = []
        for i in range(5):
            number = dice.roll()
            rolls.append(number)
            self.assertEqual(number, 0)
        self.assertEqual(dice.get_total(), sum(rolls))

    def test_roll_after_clear(self):
        rolls = []
        rolls.append(self.six_dice.roll())
        rolls.append(self.six_dice.roll())
        rolls.append(self.six_dice.roll())
        self.assertGreater(self.six_dice.get_total(), 0)
        self.six_dice.clear()
        self.assertEqual(self.six_dice.get_total(), 0)
        self.six_dice.roll()
        self.assertNotEqual(self.six_dice.get_total(), 0)

    def test_seperate_dice(self):
        dice1 = Dice(6)
        dice2 = Dice(20)
        self.assertEqual(dice1.get_total(), dice2.get_total())
        self.assertNotEqual(dice1.sides, dice2.sides)
        dice1.roll()
        dice1.roll()
        dice2.roll()
        self.assertGreater(dice1.get_total(), 0)
        self.assertGreater(dice2.get_total(), 0)
        dice2.clear()
        self.assertEqual(dice2.get_total(), 0)
        self.assertNotEqual(dice1.get_total(), 0)
        

    

if __name__ == '__main__':
    unittest.main()