import unittest
import sys
# sys.path.append('./lib')
import main

## Test genname program
## test if the path to go the first and last name are correlated to main.py
class TestConfig(unittest.TestCase):
    def test_with_default(self):
        config = main.get_config()
        self.assertDictEqual (config, {'firstname_path': './data/firstname.txt','lastname_path': './data/lastname.txt'
        })

if __name__ == "__main__":
    unittest.main()
    print ("The datasets used to generate the content are correctly located")
