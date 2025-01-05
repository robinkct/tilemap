from api import addCard, clearAllCard, getAllCardInfo
import unittest

class TestAPI(unittest.TestCase):

    def test_addCard(self):
        result = addCard.run_testcase(input=None, expect_output=None)
        self.assertEqual(result, True)

        msg = "TestAPI"
        result = addCard.run_testcase(input=msg, expect_output=None)
        self.assertEqual(result, True)

    def test_clearAllCard(self):
        result = clearAllCard.run_testcase()
        self.assertEqual(result, True)

    #def test_getAllCardInfo(self):
        #result = getAllCardInfo.run_testcase()
        #self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
