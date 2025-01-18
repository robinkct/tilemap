import unittest
from api import addCard, addConnection
from api import getCardInfoByID, getConnectionByID
from api import updateCard, updateConnection
from api import clearCardByID, clearConnectionByID
from api import getAllCardInfo, getAllConnectionInfo
from api import clearAllCard, clearAllConnection
from utils import logger

class TestAPI(unittest.TestCase):
    def test_addCard(self):
        """测试添加卡片功能"""
        logger.info("测试添加卡片")
        result = addCard.run_testcase()
        self.assertTrue(result)

        msg = "TestAPI"
        result = addCard.run_testcase(input=msg)
        self.assertTrue(result)

    def test_addConnection(self):
        """测试添加连接功能"""
        logger.info("测试添加连接")
        result = addConnection.run_testcase()
        self.assertTrue(result)

    def test_getCardInfoByID(self):
        """测试通过ID获取卡片信息"""
        logger.info("测试获取卡片信息")
        result = getCardInfoByID.run_testcase()
        self.assertTrue(result)

    def test_getConnectionByID(self):
        """测试通过ID获取连接信息"""
        logger.info("测试获取连接信息")
        result = getConnectionByID.run_testcase()
        self.assertTrue(result)

    def test_updateCard(self):
        """测试更新卡片信息"""
        logger.info("测试更新卡片")
        result = updateCard.run_testcase(id="dummy0", expect_output="UpdateCard")
        self.assertTrue(result)

    def test_updateConnection(self):
        """测试更新连接信息"""
        logger.info("测试更新连接")
        result = updateConnection.run_testcase()
        self.assertTrue(result)

    def test_clearCardByID(self):
        """测试通过ID清除卡片"""
        logger.info("测试清除指定卡片")
        result = clearCardByID.run_testcase()
        self.assertTrue(result)

    def test_clearConnectionByID(self):
        """测试通过ID清除连接"""
        logger.info("测试清除指定连接")
        result = clearConnectionByID.run_testcase()
        self.assertTrue(result)

    def test_getAllCardInfo(self):
        """测试获取所有卡片信息"""
        logger.info("测试获取所有卡片信息")
        result = getAllCardInfo.run_testcase()
        self.assertTrue(result)

    def test_getAllConnectionInfo(self):
        """测试获取所有连接信息"""
        logger.info("测试获取所有连接信息")
        result = getAllConnectionInfo.run_testcase()
        self.assertTrue(result)

    @unittest.skip("此测试会清除所有卡片，謹慎使用")
    def test_clearAllCard(self):
        """测试清除所有卡片"""
        logger.info("测试清除所有卡片")
        result = clearAllCard.run_testcase()
        self.assertTrue(result)

    @unittest.skip("此测试会清除所有連接，謹慎使用")
    def test_clearAllConnection(self):
        """测试清除所有连接"""
        logger.info("测试清除所有连接")
        result = clearAllConnection.run_testcase()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)