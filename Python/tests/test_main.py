import unittest
from main import main

class TestMain(unittest.TestCase):

    def test_main(self):
        try:
            main()
            success = True
        except Exception as e:
            success = False
            print(e)
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
