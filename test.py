import unittest
import io
import sys
from unittest.mock import patch

import flights

import os
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

class Test01_ADDFLIGHT(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** FUNCTION CALL: f.add_flight('XXX','YYY','9999','0907','Y','1509') THEN fts = f.get_flights() *** EXPECT: fts[0] == ['XXX', 'YYY', '9999', '9:07am', '+3:09pm', '6:02'] ***
        """
        remove_file('f99.dat')
        f = flights.Flights('f99.dat')
        f.add_flight('XXX','YYY','9999','0907','Y','1509')
        fts = f.get_flights()
        ft = fts[0]
        self.assertEqual(fts[0], ['XXX', 'YYY', '9999', '9:07am', '+3:09pm', '6:02'])
        remove_file('f99.dat')
        print()

class Test02_ADDFLIGHT(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** FUNCTION CALL: f.add_flight('XXX','YYY','9999','0035','N','2336') THEN fts = f.get_flights() *** EXPECT: fts[0] == ['XXX', 'YYY', '9999', '12:35am', '11:36pm', '23:01'] ***
        """
        remove_file('f99.dat')
        f = flights.Flights('f99.dat')
        f.add_flight('XXX','YYY','9999','0035','N','2336')
        fts = f.get_flights()
        ft = fts[0]
        self.assertEqual(fts[0], ['XXX', 'YYY', '9999', '12:35am', '11:36pm', '23:01'])
        remove_file('f99.dat')
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
