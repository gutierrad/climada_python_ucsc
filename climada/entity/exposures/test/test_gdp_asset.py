"""
This file is part of CLIMADA.

Copyright (C) 2017 ETH Zurich, CLIMADA contributors listed in AUTHORS.

CLIMADA is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License as published by the Free
Software Foundation, version 3.

CLIMADA is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with CLIMADA. If not, see <https://www.gnu.org/licenses/>.

Unit Tests on GDP2Asset exposures.

"""
import os
import numpy as np
import unittest
import pandas as pd
from climada.entity.exposures import gdp_asset as ga
from climada.util.constants import DATA_DIR, NAT_REG_ID


DEMO_GDP2ASSET = os.path.join(DATA_DIR, 'demo', 'gdp2asset_demo_exposure.nc')


class TestGDP2AssetClass(unittest.TestCase):
    """Unit tests for the LitPop exposure class"""
    def test_wrong_iso3_fail(self):
        """Wrong ISO3 code"""
        testGDP2A = ga.GDP2Asset()

        with self.assertRaises(KeyError):
            testGDP2A.set_countries(countries=['OYY'])
        with self.assertRaises(KeyError):
            testGDP2A.set_countries(countries=['DEU'], ref_year=2600)

class TestGDP2AssetFunctions(unittest.TestCase):
    """Test LitPop Class methods"""
    
    def test_set_one_country(self):
        exp_test = ga.GDP2Asset._set_one_country('LIE', 2000, DEMO_GDP2ASSET)
        with self.assertRaises(KeyError):
            ga.GDP2Asset._set_one_country('LIE', 2001, DEMO_GDP2ASSET)

        self.assertAlmostEqual(exp_test.iloc[0, 2], 9.5206968)
        self.assertAlmostEqual(exp_test.iloc[1, 2], 9.5623634)
        self.assertAlmostEqual(exp_test.iloc[2, 2], 9.60403)
        self.assertAlmostEqual(exp_test.iloc[3, 2], 9.5206968)
        self.assertAlmostEqual(exp_test.iloc[4, 2], 9.5623634)
        self.assertAlmostEqual(exp_test.iloc[5, 2], 9.60403)
        self.assertAlmostEqual(exp_test.iloc[6, 2], 9.5206968)
        self.assertAlmostEqual(exp_test.iloc[7, 2], 9.5623634)
        self.assertAlmostEqual(exp_test.iloc[8, 2], 9.60403)
        self.assertAlmostEqual(exp_test.iloc[9, 2], 9.5206968)
        self.assertAlmostEqual(exp_test.iloc[10, 2], 9.5623634)
        self.assertAlmostEqual(exp_test.iloc[11, 2], 9.5206968)
        self.assertAlmostEqual(exp_test.iloc[12, 2], 9.5623634)
        
        self.assertAlmostEqual(exp_test.iloc[0, 1], 47.0622474)
        self.assertAlmostEqual(exp_test.iloc[1, 1], 47.0622474)
        self.assertAlmostEqual(exp_test.iloc[2, 1], 47.0622474)
        self.assertAlmostEqual(exp_test.iloc[3, 1], 47.103914)
        self.assertAlmostEqual(exp_test.iloc[4, 1], 47.103914)
        self.assertAlmostEqual(exp_test.iloc[5, 1], 47.103914)
        self.assertAlmostEqual(exp_test.iloc[6, 1], 47.1455806)
        self.assertAlmostEqual(exp_test.iloc[7, 1], 47.1455806)
        self.assertAlmostEqual(exp_test.iloc[8, 1], 47.1455806)
        self.assertAlmostEqual(exp_test.iloc[9, 1], 47.1872472)
        self.assertAlmostEqual(exp_test.iloc[10, 1], 47.1872472)
        self.assertAlmostEqual(exp_test.iloc[11, 1], 47.2289138)
        self.assertAlmostEqual(exp_test.iloc[12, 1], 47.2289138)
        
        self.assertAlmostEqual(exp_test.iloc[0, 0], 174032107.65846416)
        self.assertAlmostEqual(exp_test.iloc[1, 0], 20386409.991937194)
        self.assertAlmostEqual(exp_test.iloc[2, 0], 2465206.6989314994)
        self.assertAlmostEqual(exp_test.iloc[3, 0], 0.0)
        self.assertAlmostEqual(exp_test.iloc[4, 0], 12003959.733058406)
        self.assertAlmostEqual(exp_test.iloc[5, 0], 97119771.42771776)
        self.assertAlmostEqual(exp_test.iloc[6, 0], 0.0)
        self.assertAlmostEqual(exp_test.iloc[7, 0], 4137081.3646739507)
        self.assertAlmostEqual(exp_test.iloc[8, 0], 27411196.308422357)
        self.assertAlmostEqual(exp_test.iloc[9, 0], 0.0)
        self.assertAlmostEqual(exp_test.iloc[10, 0], 4125847.312198318)
        self.assertAlmostEqual(exp_test.iloc[11, 0], 88557558.43543366)
        self.assertAlmostEqual(exp_test.iloc[12, 0], 191881403.05181965)

        self.assertAlmostEqual(exp_test.iloc[0, 3], 3.0)
        self.assertAlmostEqual(exp_test.iloc[12, 3], 3.0)
        self.assertAlmostEqual(exp_test.iloc[0, 4], 11.0)
        self.assertAlmostEqual(exp_test.iloc[12, 4], 11.0)

    def test_fast_if_mapping(self):

        testIDs = pd.read_csv(NAT_REG_ID)
        self.assertAlmostEqual(ga._fast_if_mapping(1, testIDs)[0], 2.0)
        self.assertAlmostEqual(ga._fast_if_mapping(1, testIDs)[1], 6.0)

        self.assertAlmostEqual(ga._fast_if_mapping(45, testIDs)[0], 5.0)
        self.assertAlmostEqual(ga._fast_if_mapping(45, testIDs)[1], 1.0)

        self.assertAlmostEqual(ga._fast_if_mapping(124, testIDs)[0], 0.0)
        self.assertAlmostEqual(ga._fast_if_mapping(124, testIDs)[1], 2.0)

    def test_read_GDP(self):

        exp_test = ga.GDP2Asset._set_one_country('LIE', 2000, DEMO_GDP2ASSET)
        coordinates = np.zeros((exp_test.shape[0], 2))
        coordinates[:, 0] = np.array(exp_test['latitude'])
        coordinates[:, 1] = np.array(exp_test['longitude'])

        with self.assertRaises(KeyError):
            ga._read_GDP(coordinates, ref_year=2600)

        testAssets = ga._read_GDP(coordinates, ref_year=2000)

        self.assertAlmostEqual(testAssets[0], 174032107.65846416)
        self.assertAlmostEqual(testAssets[1], 20386409.991937194)
        self.assertAlmostEqual(testAssets[2], 2465206.6989314994)
        self.assertAlmostEqual(testAssets[3], 0.0)
        self.assertAlmostEqual(testAssets[4], 12003959.733058406)
        self.assertAlmostEqual(testAssets[5], 97119771.42771776)
        self.assertAlmostEqual(testAssets[6], 0.0)
        self.assertAlmostEqual(testAssets[7], 4137081.3646739507)
        self.assertAlmostEqual(testAssets[8], 27411196.308422357)
        self.assertAlmostEqual(testAssets[9], 0.0)
        self.assertAlmostEqual(testAssets[10], 4125847.312198318)
        self.assertAlmostEqual(testAssets[11], 88557558.43543366)
        self.assertAlmostEqual(testAssets[12], 191881403.05181965)


if __name__ == "__main__":
    TESTS = unittest.TestLoader().loadTestsFromTestCase(TestGDP2AssetFunctions)
    TESTS.addTests(unittest.TestLoader().loadTestsFromTestCase(TestGDP2AssetClass))
    unittest.TextTestRunner(verbosity=2).run(TESTS)
