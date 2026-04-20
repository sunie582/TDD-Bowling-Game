import unittest
from bowling_game import Game

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.g = Game()

    def roll_many(self, n, pins):
        for _ in range(n):
            self.g.roll(pins)

    def test_gutter_game(self):
        """Тест: все броски в ноль (Gutter Game)"""
        self.roll_many(20, 0)
        self.assertEqual(self.g.score(), 0)

if __name__ == '__main__':
    unittest.main()