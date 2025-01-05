from api import addCard, updateCard, getAllCardInfo, getCardInfoByID
from api import addConnection, updateConnection, getAllConnectionInfo
from api import clearAllCard, clearAllConnection
import unittest

class TestAPI(unittest.TestCase):

    def test_addCard(self):
        result = addCard.run_testcase()
        self.assertEqual(result, True)

        msg = "TestAPI"
        result = addCard.run_testcase(input=msg)
        self.assertEqual(result, True)

    # Commented out because it clears all cards
    #def test_clearAllCard(self):
    #    result = clearAllCard.run_testcase()
    #    self.assertEqual(result, True)

    def test_getAllCardInfo(self):
        result = getAllCardInfo.run_testcase()
        self.assertEqual(result, True)

    def test_getCardInfoByID(self):
        result = getCardInfoByID.run_testcase()
        self.assertEqual(result, True)

    def test_updateCard(self):
        result = updateCard.run_testcase(id="dummy0", expect_output="UpdateCard")
        self.assertEqual(result, True)

    def test_addConnection(self):
        result = addConnection.run_testcase()
        self.assertEqual(result, True)

    def test_getAllConnectionInfo(self):
        result = getAllConnectionInfo.run_testcase()
        self.assertEqual(result, True)

    def test_updateConnection(self):
        result = updateConnection.run_testcase()
        self.assertEqual(result, True)

    def test_clearAllConnection(self):
        result = clearAllConnection.run_testcase()
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()