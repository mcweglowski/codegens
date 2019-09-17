import unittest
from codegen.core.configreader import readcodeitems

class Test_core_configreader(unittest.TestCase):
    def test_readcodeitems(self):
        expected = 2
        codeitems = readcodeitems()
        actual = len(codeitems)

        assert expected == actual

if __name__ == '__main__':
    unittest.main()
