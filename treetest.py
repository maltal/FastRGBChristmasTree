import unittest
from tree import FastRGBChristmasTree

class TestFastRGBChristmasTree(unittest.TestCase):

    def setUp(self):
        self.tree = FastRGBChristmasTree()

    def test_len(self):
        self.assertEqual(len(self.tree), 25)

    def test_star(self):
        self.tree.star = [255, 255, 255]
        self.assertEqual(self.tree.star, [255, 255, 255])

    def test_off(self):
        self.tree.off()
        self.assertEqual(self.tree[:], [[0, 0, 0, 0]] * 25)
        self.assertEqual(self.tree.star, [0, 0, 0, 0])

    def test_commit(self):
        self.tree[:] = [[255, 0, 0, 0]] * 25
        self.tree.commit()
        self.assertEqual(self.tree[:], [[255, 0, 0, 0]] * 25)

    def test_brightness(self):
        self.tree.brightness = 10
        self.assertEqual(self.tree.brightness, 10)

    def test_reset(self):
        self.tree.reset()
        self.assertEqual(self.tree[:], [[0, 0, 0, 0]] * 25)

if __name__ == '__main__':
    unittest.main()