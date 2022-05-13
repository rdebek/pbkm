import unittest
from task import Authenticator

class UnitTests(unittest.TestCase):
    
    def test_good_login_and_pass(self):
        self.assertTrue(Authenticator.login('admin', 'HelloWorld!'))

    def test_wrong_login_correct_pass(self):
        self.assertFalse(Authenticator.login('admin252525', 'HelloWorld!'))


    def test_correct_login_wrong_pass(self):
        self.assertFalse(Authenticator.login('admin', '1232323'))


    def test_wrong_login_and_wrong_pass(self):
        self.assertFalse(Authenticator.login('123', '555'))



if __name__ == "__main__":
        unittest.main()