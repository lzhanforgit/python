#导入unittest模块
import unittest
from calculate_func import *
from parameterized import parameterized

class TestCalculateFunc(unittest.TestCase):
    """Test mathfuc.py"""
    # num = 1
    @parameterized.expand(
        [
            ['xiaogang', '123456', True],  # 可以是list，也可以是元祖
            ['', '123456', True],
            ['xiaogang', '', False],
            ['adgadg', '123456', False]
        ]
    )

    # def setUp(self):
    #     print("do something before test.Prepare environment.")
    #
    # def tearDown(self):
    #     print("do something after test.Clean up.")
    # @classmethod
    # def setUpClass(cls):
    #     print("This setUpClass() method only called once.")
    #     # cls.num=0
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("This tearDownClass() method only called once too.")
    #     # cls.num=2


    def test_login(self, username, passwd, flag):  # 这里的参数对应上述列表里的元素，运行的时候会遍历上述列表里的二维列表直到所有元素都调用运行完成
        '''登录'''
        res = login(username, passwd)
        self.assertEqual(res, flag)

    # @unittest.skipIf(num>0,"num的值没有大于零")  #此处调用类属性不需要加类名
    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(2, add(2, 2))


    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))
    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))
    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

    def login(self):  # 注意，这里不以test开头命名，就是一普通方法，在执行测试用例的时候并不会运行，调用的时候才会
        res = login('vip001', '123456')
        self.assertEqual(res, 'vip')
        return res

    def test_login_cj(self):
        res = self.login()  # 调用登录方法，获取sign
        self.jp = buy(res)
        self.assertEqual(self.jp, True)
if __name__ == '__main__':
    unittest.main(verbosity=2)