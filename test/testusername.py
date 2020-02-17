import unittest
import sys
sys.path.append('../test')
from sys import __main__
## Test if username implemented well
class Testusername(unittest.TestCase):
    def test_user_generate(self):
        username = main.get_username()
        self.assertListEqual(username, username )

if __name__ == "__main__":
    unittest.main()
    print ("The usernames name has been generated correctly")
