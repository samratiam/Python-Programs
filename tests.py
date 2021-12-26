import unittest

#function to be tested
def add(x,y):
    return x+y

class TestAdd(unittest.TestCase):
    def test_positive(self): #test method must begin with test
        #test 2+6 equals 6
        self.assertEqual(add(2,6),8)

    def test_negative(self):
        #tests 2+6 isnot equal to 7
        self.assertNotEqual(add(2,6),7)
if __name__ == '__main__':
    unittest.main()

#to run add tests in Test Add class use command
#python -m unittest tests.TestAdd
#if it gives dots(...) as output its fine
#if it gives f as an output its failed

#run test_positive test only
#python -m tests.TestAdd.test_positive