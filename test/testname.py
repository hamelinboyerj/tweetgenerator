import unittest
import sys
sys.path.append('./lib')
import main

## Test if first name implemented well
class TestFirstNameGeneration(unittest.TestCase):
    def test_user_generate(self):
        firstname = main.get_newfirstname()
        self.assertDictContainsSubset(firstname, {'firstname_path' : './data/original/firstname.txt'
        })

    def test_lastname_generate(self):
        lastname = main.get_newlastname()
        self.assertDictContainsSubset(lastname,{'lastname_path':'./data/original/lastname.txt'
        })

if __name__ == "__main__":
    unittest.main()
    print ("The usernames name has been generated correctly")
