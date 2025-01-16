import unittest
from animals_leg_count import count_four_legged_animals

class TestCountFourLeggedAnimals(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(count_four_legged_animals(['lion', 'monkey', 'deer', 'snake', 'elephant']), 3)
        self.assertEqual(count_four_legged_animals(['frog', 'horse', 'spider', 'ant']), 1)
        self.assertEqual(count_four_legged_animals(['dog', 'cat', 'lion', 'deer', 'horse', 'elephant']), 6)

if __name__ == 'main':
    unittest.main()