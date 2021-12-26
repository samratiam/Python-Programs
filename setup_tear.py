import unittest

class Demo:
    cls_var1 = "Kobe"
    cls_var2 = "Bryant"
    cls_var3 = 21

    @staticmethod
    def two():
        return 2

    def __str__(self):
        return "test"
class TestDemo(unittest.TestCase):
    def setUp(self)->None:   #gives error before testing if there
        #creating an object of Demo class
        self.demo = Demo()

    def test_cls_variables(self):
        #tests class variables
        self.assertEqual(self.demo.cls_var1,'Kobe')
        self.assertEqual(self.demo.cls_var2,'Bryant')
        self.assertEqual(self.demo.cls_var3,21)

    def test_str(self):
        #test string representation
        self.assertEqual(self.demo.__str__(),'test')

    @unittest.skip("demonstrating skipping")
    #this test is skipped
    def test_nothing(self):
        print("Skip this")

    def test_two(self):
        #tests static method two()
        self.assertEqual(self.demo.two(),2)
        self.assertNotEqual(self.demo.two(),3)

    def tearDown(self)->None:
        #deleting the object
        del self.demo

#command to run
#python -m unittest setup_tear
