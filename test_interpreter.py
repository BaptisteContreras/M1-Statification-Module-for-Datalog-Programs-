#! /usr/bin/env python3
import pytest
import glob
import os
import sys
from test_expect_pragma import TestExpectPragmas, cat

HERE = os.path.dirname(os.path.realpath(__file__))
if HERE == os.path.realpath('.'):
    HERE = '.'
TEST_DIR = HERE
IMPLEM_DIR = HERE


ALL_FILES = []
# tests for typing AND evaluation
# change here to also include bad_def tests.
ALL_FILES += glob.glob(TEST_DIR + '/test/*.txt')


# Path setting
if 'TEST_FILES' in os.environ:
    ALL_FILES = glob.glob(os.environ['TEST_FILES'], recursive=True)
STRATIF_EVAL = os.path.join(IMPLEM_DIR, 'Main.py')


class TestInterpret(TestExpectPragmas):

    def evaluate(self, file):
        return self.run_command(['python3', STRATIF_EVAL, file])

    # Not in test_expect_pragma to get assertion rewritting
    def assert_equal(self, actual, expected):
        if expected.output is not None and actual.output is not None:
            assert actual.output == expected.output, \
                "Output of the program is incorrect."
        assert actual.exitcode == expected.exitcode, \
            "Exit code of the compiler is incorrect"
        assert actual.execcode == expected.execcode, \
            "Exit code of the execution is incorrect"

    @pytest.mark.parametrize('filename', ALL_FILES)
    def test_eval(self, filename):
        cat(filename)  # For diagnosis
        expect = self.get_expect(filename)
        eval = self.evaluate(filename)
        if expect:
            self.assert_equal(eval, expect)


if __name__ == '__main__':
    pytest.main(sys.argv)
