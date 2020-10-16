import unittest
from excel import excel_reader
from config import config

class test_excel(unittest.TestCase):
    def test_excel_reader_read(self):
        config_data = config.config('SampleData.xlsx', ['Fields', 'ConstantTextDefs'], None, 6, 'A', 'C')
        rowsets = excel_reader.read(config_data)

        rowset = rowsets['Fields']
        assert 4          == len(rowset)
        assert "UserName" == rowset[0][0].value
        assert 0          == rowset[0][1].value
        assert "string"   == rowset[0][2].value
        assert "Addres1"  == rowset[1][0].value
        assert 1          == rowset[1][1].value
        assert "string"   == rowset[1][2].value
        assert "Age"      == rowset[2][0].value
        assert 2          == rowset[2][1].value
        assert "int"      == rowset[2][2].value
        assert "City"     == rowset[3][0].value
        assert 3          == rowset[3][1].value
        assert "string"   == rowset[3][2].value
        
if __name__ == '__main__':
    unittest.main()