import unittest
from api import addCard, addConnection
from api import getCardInfoByID, getConnectionByID
from api import updateCard, updateConnection
from api import clearCardByID, clearConnectionByID
from api import getAllCardInfo, getAllConnectionInfo
from api import clearAllCard, clearAllConnection
from utils import logger

class TestAPI(unittest.TestCase):
    def setUp(self):
        """測試前的設置"""
        self.verbose = False  # 控制是否顯示詳細日誌

    def test_addCard(self):
        """測試添加卡片功能"""
        if self.verbose:
            logger.info("測試添加卡片")
        result = addCard.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

        msg = "TestAPI"
        result = addCard.run_testcase(input=msg, verbose=self.verbose)
        self.assertTrue(result)

    def test_addConnection(self):
        """測試添加連接功能"""
        if self.verbose:
            logger.info("測試添加連接")
        result = addConnection.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

    def test_getCardInfoByID(self):
        """測試通過ID獲取卡片信息"""
        if self.verbose:
            logger.info("測試獲取卡片信息")
        result = getCardInfoByID.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

    def test_getConnectionByID(self):
        """測試通過ID獲取連接信息"""
        if self.verbose:
            logger.info("測試獲取連接信息")
        result = getConnectionByID.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

    def test_updateCard(self):
        """測試更新卡片信息"""
        if self.verbose:
            logger.info("測試更新卡片")
        result = updateCard.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

    def test_updateConnection(self):
        """測試更新連接信息"""
        if self.verbose:
            logger.info("測試更新連接")
        result = updateConnection.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

    def test_clearCardByID(self):
        """測試通過ID清除卡片"""
        if self.verbose:
            logger.info("測試清除指定卡片")
        result = clearCardByID.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

    def test_clearConnectionByID(self):
        """測試通過ID清除連接"""
        if self.verbose:
            logger.info("測試清除指定連接")
        result = clearConnectionByID.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

    def test_getAllCardInfo(self):
        """測試獲取所有卡片信息"""
        if self.verbose:
            logger.info("測試獲取所有卡片信息")
        result = getAllCardInfo.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

    def test_getAllConnectionInfo(self):
        """測試獲取所有連接信息"""
        if self.verbose:
            logger.info("測試獲取所有連接信息")
        result = getAllConnectionInfo.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

    @unittest.skip("此測試會清除所有卡片，謹慎使用")
    def test_clearAllCard(self):
        """測試清除所有卡片"""
        if self.verbose:
            logger.info("測試清除所有卡片")
        result = clearAllCard.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

    @unittest.skip("此測試會清除所有連接，謹慎使用")
    def test_clearAllConnection(self):
        """測試清除所有連接"""
        if self.verbose:
            logger.info("測試清除所有連接")
        result = clearAllConnection.run_testcase(verbose=self.verbose)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)