import unittest

# from fileName import className
from AddSubClassDemo import AddSub


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("This will run once before all the methods")

    @classmethod
    def tearDownClass(cls) -> None:
        print("This will run once after all methods")
    def setUp(self) -> None:
        print("This will run before every method")

    def tearDown(self) -> None:
        print("This will run after every method")

    def test_add(self):
        result = AddSub.add(self,10,20)
        self.assertEqual(result, 30)

    def test_sub(self):
        result = AddSub.sub(self, 10,20)
        self.assertEqual(result, -10)


    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here


# if __name__ == '__main__':
#     unittest.main()


# terminal test

# python -m unittest PythonUnitTestDemo.py