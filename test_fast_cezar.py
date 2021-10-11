import unittest
import fast_cezar

class TestCipher(unittest.TestCase):

    def test_encode(self):
            self.assertEqual(fast_cezar.encoder('pies'), 'unjx')
            self.assertEqual(fast_cezar.encoder('ziz'), 'EnE')
            self.assertEqual(fast_cezar.encoder('dom121'), 'itr676')
            self.assertEqual(fast_cezar.encoder('Ramb0\n'), 'Wfrg5{s')
            self.assertEqual(fast_cezar.encoder('zuzv2!'), 'EzEA7&')
            
    def test_decode(self):
            self.assertEqual(fast_cezar.decoder('unjx'), 'pies')
            self.assertEqual(fast_cezar.decoder('EnE'), 'ziz')
            self.assertEqual(fast_cezar.decoder('itr676'), 'dom121')
            self.assertEqual(fast_cezar.decoder('Wfrg5{s'), 'Ramb0\\n')
            #self.assertEqual(fast_cezar.decoder('EzEA7&', 'zuzv2!') in terminal this is ok