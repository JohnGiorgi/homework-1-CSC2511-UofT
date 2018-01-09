import unittest
from a1_preproc import preproc1

class A1PreprocTestCase(unittest.TestCase):
    """Unit tests for a1_preproc.py."""

    def test_step1(self):
        self.assertIsInstance(preproc1('This is a string, right?', steps=[1]), str)
        self.assertEqual(preproc1('Test trailing\n', steps=[1]), 'Test trailing')
        self.assertEqual(preproc1('\nTest proceeding', steps=[1]), 'Test proceeding')
        self.assertEqual(preproc1('\nTest\nin\nbetween\n', steps=[1]), 'Test in between')
    def test_step2(self):
        self.assertIsInstance(preproc1('This is a string, right?', steps=[2]), str)
        self.assertEqual(preproc1('Simple test: &#33', steps=[2]), 'Simple test: !')
        self.assertEqual(preproc1("Hard test: I can&#39t believe that&#44 this actually works&#33&#63", steps=[2]),
            "Hard test: I can't believe that, this actually works!?")
    def test_step3(self):
        self.assertIsInstance(preproc1('This is a string, right?', steps=[3]), str)
        self.assertEqual(preproc1('I found it on this site, www.conspiracytheory.net', steps=[3]),
        'I found it on this site, ')
        self.assertEqual(preproc1('I found it on this site, http://conspiracytheory.net', steps=[3]),
        'I found it on this site, ')
        self.assertEqual(preproc1('I found it on this site, https://conspiracytheory.net', steps=[3]),
        'I found it on this site, ')
        self.assertEqual(preproc1('I found it on this site, https://conspiracytheory.com', steps=[3]),
        'I found it on this site, ')
        # check multiple URLs
        self.assertEqual(preproc1('I found it on this site, https://conspiracytheory.com. Also checkout this site, www.infowars.com', steps=[3]),
        'I found it on this site, . Also checkout this site, ')
    def test_step4(self):
        self.assertIsInstance(preproc1('This is a string, right?', steps=[4]), str)
        pass
    def test_step5(self):
        self.assertIsInstance(preproc1('This is a string, right?', steps=[5]), str)
        pass
    def test_step6(self):
        self.assertIsInstance(preproc1('This is a string, right?', steps=[6]), str)
        pass
    def test_step7(self):
        self.assertIsInstance(preproc1('This is a string, right?', steps=[7]), str)
        self.assertEqual(preproc1('all must go', steps=[7]), '  ')
        self.assertEqual(preproc1('some of these  must go', steps=[7]), '   words  ')
    def test_step8(self):
        self.assertIsInstance(preproc1('This is a string, right?', steps=[8]), str)
        pass
    def test_step9(self):
        self.assertIsInstance(preproc1('This is a string, right?', steps=[9]), str)
        pass
    def test_step10(self):
        self.assertIsInstance(preproc1('This is a string, right?', steps=[10]), str)
        self.assertEqual(preproc1('sImpLe TEST', steps=[10]), 'simple test')
        self.assertEqual(preproc1('FOR GOOD MEASURE', steps=[10]), 'for good measure')

    def tearDown(self):
        modComm = ''

if __name__ == '__main__':
    unittest.main()
