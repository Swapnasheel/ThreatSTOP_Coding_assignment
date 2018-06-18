'''
UNIT test for the assignment program.
'''

import unittest
from assignment import *
import os

class Test(unittest.TestCase):

    def setUp(self):
        self.obj = Parse()

    def tearDown(self):
        pass

    def test_get_process(self):
        cmd = 'pwd'
        out = self.obj.get_process_out(cmd)

        self.assertEquals(out, os.getcwd()+'\n')

    def test_ip_add_parsing(self):
        cmd = "ANSWER SECTION:\nacls.threatstop.local.\t604800\tIN\tA\t10.1.227.35\n"
        out = self.obj.parse_ip_addresses(cmd)

        self.assertEquals(out[0], '10.1.227.35')

        #Negative test
        self.assertNotEqual(out[0], '192.168.0.1')

    def test_non_A_records(self):
        '''
        To verify program only takes A records and not AAA records.
        '''
        cmd = "ANSWER SECTION:\nwww.google.com.\t265\tIN\tAAAA\t2607:f8b0:4007:808::2004\n"
        out = self.obj.parse_ip_addresses(cmd)
        self.assertEqual(out, [])



if __name__ == "__main__":
    unittest.main()
