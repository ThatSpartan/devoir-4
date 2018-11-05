import unittest
from d4q2Lib import *

class MyTest(unittest.TestCase):

    def test_effaceTableau(self):
        tableau = [
            ['x', 'o', 'x'],
            ['-', 'x', 'o'],
            ['-', '-', '-']
        ]
        effaceTableau(tableau)
        self.assertEqual(tableau, [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']])

    def testLignes(self):
        tableau = [
            ['x', 'x', 'x'],
            ['y', 'x', 'x'],
            ['z', 'x', 'x'],
        ]
        testLignes(tableau)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
