import unittest
import os
import os.path
import sys
sys.path.append('../generator')

## Test genname program
## test if the path to go the first and last name are correlated to main.py
class TestGeneration(unittest.TestCase):
    # def test_with_default(self):
    #     # This is for testing main parameters: correct location of data source
    #     config = main.get_config()
    #     self.assertDictEqual (config, {'firstname_path': './data/firstname.txt','lastname_path': './data/lastname.txt'
    #     })

    def setUp(self):
        sys.path.insert(0, "../generator")
        from generator import genname

    def test_user_generate(self):
        #This is for testing the generation of a new user.
        username_data = self.main()
        self.assertListEqual(username_data, username_data )
    #
    # def test_country_generate(self):
    #


if __name__ == "__main__":
    unittest.main()
    print ("The usernames name has been generated correctly")
