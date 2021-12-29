import unittest
import app

class TestGetData(unittest.TestCase):
    def setUp(self):
        print('+ テスト開始')

    def tearDown(self):
        print('+ テスト終了')

    def test_get_data(self):
        tickers = {
            'apple': 'AAPL',
            'google': 'GOOGL',
            'microsoft': 'MSFT',
            'amazon': 'AMZN',
        }
        self.assertIsNotNone(app.get_data(1,tickers))
        self.assertIsNotNone(app.get_data(50, tickers))

if __name__ == '__main__':
    unittest.main()
