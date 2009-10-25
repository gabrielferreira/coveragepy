"""Tests that our test infrastructure is really working!"""

import os, sys
sys.path.insert(0, os.path.split(__file__)[0]) # Force relative import for Py3k
from coveragetest import CoverageTest

class TestingTest(CoverageTest):
    """Tests of helper methods on CoverageTest."""

    def test_assert_equal_sets(self):
        self.assert_equal_sets(set(), set())
        self.assert_equal_sets(set([1,2,3]), set([3,1,2]))
        self.assertRaises(AssertionError, self.assert_equal_sets,
            set([1,2,3]), set()
            )
        self.assertRaises(AssertionError, self.assert_equal_sets,
            set([1,2,3]), set([4,5,6])
            )

    def test_assert_matches(self):
        self.assert_matches("hello", "hel*o")
        self.assert_matches("Oh, hello there!", "hel*o")
        self.assertRaises(AssertionError, self.assert_matches,
            "hello there", "^hello$"
            )
