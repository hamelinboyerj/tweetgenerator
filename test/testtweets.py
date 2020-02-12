import unittest
import sys
sys.path.append('./lib')
import main

class Testgentweet(unittest.TestCase):
    def test_validate_input_type_string(self):
        newtweet = main.get_newtweet()
        self.assertDictEqual (newtweet, {'newtweet_path': './data/tweetuser.csv'
        })

if __name__ == '__main__':
        unittest.main()
