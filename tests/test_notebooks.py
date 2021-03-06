import os
import testipynb
import unittest
import numpy as np

NBDIR = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-2]
)

Test = testipynb.TestNotebooks(directory=NBDIR, timeout=2800)
TestNotebooks = Test.get_tests()

if __name__ == "__main__":
    unittest.main()
