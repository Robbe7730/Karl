# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest

from planet import FutureIterator

class TestFutureIterator(unittest.TestCase):

    def test_no_expeditions(self):
        iterator = FutureIterator(1, [], True)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 4)

    def test_one_expedition(self):
        iterator = FutureIterator(10, [make_expedition(3, 5)], False)
        self.assertEqual(next(iterator), 11)
        self.assertEqual(next(iterator), 12)
        self.assertEqual(next(iterator), 8)
        self.assertEqual(next(iterator), 9)

    def test_two_expedition(self):
        iterator = FutureIterator(10, [
            make_expedition(3, 5),
            make_expedition(4, 5)
        ], False)
        self.assertEqual(next(iterator), 11)
        self.assertEqual(next(iterator), 12)
        self.assertEqual(next(iterator), 8)
        self.assertEqual(next(iterator), 4)

    def test_distress(self):
        iterator = FutureIterator(10, [
            make_expedition(3, 50),
        ], True)
        self.assertEqual(next(iterator), 11)
        self.assertEqual(next(iterator), 12)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(iterator.distress_count, 38)

        iterator = FutureIterator(1, [
            make_expedition(1, 5),
        ], True)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(iterator.distress_count, 4)

    def test_distress_zero(self):
        iterator = FutureIterator(10, [
            make_expedition(3, 13),
        ], True)
        self.assertEqual(next(iterator), 11)
        self.assertEqual(next(iterator), 12)
        self.assertEqual(next(iterator), 1)

    def test_reinforcements(self):
        iterator = FutureIterator(10, [
            make_expedition(3, 2, 1),
        ], True)
        self.assertEqual(next(iterator), 11)
        self.assertEqual(next(iterator), 12)
        self.assertEqual(next(iterator), 15)

    def test_recover(self):
        iterator = FutureIterator(10, [
            make_expedition(3, 15),
        ], False)
        self.assertEqual(next(iterator), 11)
        self.assertEqual(next(iterator), 12)
        self.assertEqual(next(iterator), -2)

    def test_multiple_arrival(self):
        iterator = FutureIterator(4, [
            make_expedition(1, 5, 2),
            make_expedition(1, 5, 3),
        ], False)
        self.assertEqual(next(iterator), 0)

        iterator = FutureIterator(3, [
            make_expedition(1, 3, 2),
            make_expedition(1, 5, 3),
        ], False)
        self.assertEqual(next(iterator), -1)


def make_expedition(turns_remaining, ship_count, owner=2):
    return {
        "owner": owner,
        "ship_count": ship_count,
        "turns_remaining": turns_remaining,
        "destination": "You",
        "origin": "Me",
    }

if __name__ == '__main__':
    unittest.main()
