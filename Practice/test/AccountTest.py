import unittest

from PythonWithChibuzo import Account


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.account = Account("David Silver", "1234")

    def test_depositMoneyWorks(self):
        self.account.deposit(250.0)
        self.assertEqual(250.0, self.account.check_balance("1234"))

    def test_withdrawMoney(self):
        self.account.deposit(250.0)
        self.account.withdraw(100.0, "1234")
        self.assertEqual(150.0, self.account.check_balance("1234"))


if __name__ == '__main__':
    unittest.main()
