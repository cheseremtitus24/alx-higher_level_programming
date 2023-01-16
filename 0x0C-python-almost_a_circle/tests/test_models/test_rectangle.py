#!/usr/bin/python3
import io
import sys
import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        self.Rectangle = __import__('models').rectangle.Rectangle

    def tearDown(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        del self.b0
        del self.Rectangle

    def test_that_on_init_values_are_set(self):
        """ Test that Values are set when initialized """
        self.b0 = self.Rectangle(3, 4, 5, 7, 2)
        self.assertEqual(self.b0.width, 3)
        self.assertEqual(self.b0.height, 4)
        self.assertEqual(self.b0.x, 5)
        self.assertEqual(self.b0.y, 7)
        self.assertEqual(self.b0.id, 2)

    def test_that_on_update_values_are_set(self):
        """ Test that on Update Values are set"""

        # instantiate Rectangle instance
        self.b0 = self.Rectangle(3, 4, 5, 7, 2)

        self.update_val = 22

        # Update width
        self.b0.width = self.update_val
        # verify update change
        self.assertEqual(self.b0.width, self.update_val)

        # Update height
        self.b0.height = self.update_val
        # verify update change
        self.assertEqual(self.b0.height, self.update_val)

        # Update x
        self.b0.x = self.update_val
        # verify update change
        self.assertEqual(self.b0.x, self.update_val)

        # Update y
        self.b0.y = self.update_val
        # verify update change
        self.assertEqual(self.b0.y, self.update_val)

        # Update id
        self.b0.id = self.update_val
        # verify update change
        self.assertEqual(self.b0.id, self.update_val)

    # @unittest.skip("always skip this test")
    def test_data_type_on_init(self):
        """Performs test instantiation values to ensure values are integers
        parameters passed in are :
        width (int): tested
        height (int): tested
        x (int): tested
        y (int): tested
        id (int) - Not Tested
        """
        self.b0 = None

        # test width
        with self.assertRaises(TypeError):
            self.Rectangle(False, 2)
        # test height
        with self.assertRaises(TypeError):
            self.Rectangle(10, True)
        # test x
        with self.assertRaises(TypeError):
            self.Rectangle(10, 2, True, 0, 0)
        # test y
        with self.assertRaises(TypeError):
            self.Rectangle(10, 2, 0, True, 0)

    # @unittest.skip("always skip this test")
    def test_data_type_on_setting(self):
        """
        Verifies that parameters are being checked against the allowed data types
        """
        self.b0 = None
        r = self.Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(ValueError):
            r.height = -10
        with self.assertRaises(ValueError):
            r.x = -10
        with self.assertRaises(ValueError):
            r.y = -10

    # @unittest.skip("always skip this test")
    def test_data_value_on_init(self):
        """
        Verifies that on initialization the int data types is enforced
        :return:
        """
        self.b0 = None
        # test x
        with self.assertRaises(ValueError):
            self.Rectangle(10, 2, -1, 0, 0)
        # test y
        with self.assertRaises(ValueError):
            self.Rectangle(10, 2, 0, -1, 0)
        # test width
        with self.assertRaises(ValueError):
            self.Rectangle(10, 2, -1, -1, 0)
        # test height
        with self.assertRaises(ValueError):
            self.Rectangle(10, 2, 1, -1, 0)

    # @unittest.skip("always skip this test")
    # def test_id_autogen(self):
    #     # id is a positive number
    #     self.b0 = self.Rectangle(3)
    #     self.assertEqual(self.b0.id, 3)
    #
    #     # id is zero
    #     self.b0 = self.Rectangle(0)
    #     self.assertEqual(self.b0.id, 1)
    #
    #     # id is negative
    #     self.b0 = self.Rectangle(-1)
    #     self.assertEqual(self.b0.id, 2)
    #
    #     # id is a non integer
    #     self.b0 = self.Rectangle(True)
    #     self.assertEqual(self.b0.id, 3)


class TestRectangleArea(unittest.TestCase):
    def setUp(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        self.Rectangle = __import__('models').rectangle.Rectangle

    def tearDown(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        del self.b0
        del self.Rectangle

    def test_area_of_rectangle(self):
        self.b0 = self.Rectangle(2, 4)
        self.assertEqual(self.b0.area(), 8)

        self.b0 = self.Rectangle(5, 3)
        self.assertEqual(self.b0.area(), 15)

        self.b0 = self.Rectangle(4, 4)
        self.assertEqual(self.b0.area(), 16)

        self.b0 = self.Rectangle(0, 7)
        self.assertEqual(self.b0.area(), 0)

        self.b0 = self.Rectangle(7, 0)
        self.assertEqual(self.b0.area(), 0)

    def test_area_of_rectangle_with_negative_value(self):
        self.b0 = None
        with self.assertRaises(ValueError):
            self.b0 = self.Rectangle(-2, 4)
            self.b0.area()

        with self.assertRaises(ValueError):
            self.b0 = self.Rectangle(3, -4)
            self.b0.area()

        with self.assertRaises(ValueError):
            self.b0 = self.Rectangle(-4, 4)
            self.b0.area()

        with self.assertRaises(ValueError):
            self.b0 = self.Rectangle(-2, -4)
            self.b0.area()

    def test_area_of_rectangle_with_zero_value(self):
        self.b0 = self.Rectangle(0, 0)
        self.assertEqual(self.b0.area(), 0)


class TestRectangleDisplay(unittest.TestCase):
    def setUp(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        self.Rectangle = __import__('models').rectangle.Rectangle

    def tearDown(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        del self.b0
        del self.Rectangle

    def test_stdout_square(self):
        # redirect stdout to a buffer
        sys.stdout = io.StringIO()
        # call the function that should print something
        self.b0 = self.Rectangle(2, 2)
        self.b0.display()
        # get the contents of the buffer
        output = sys.stdout.getvalue()
        # check the contents against expected output
        self.assertEqual(output, "##\n##\n")
        # reset stdout
        sys.stdout = sys.__stdout__

    def test_stdout_rectangle(self):
        # redirect stdout to a buffer
        sys.stdout = io.StringIO()
        # call the function that should print something
        self.b0 = self.Rectangle(4, 6)
        self.b0.display()
        # get the contents of the buffer
        output = sys.stdout.getvalue()
        # check the contents against expected output
        self.assertEqual(output, "####\n####\n####\n####\n####\n####\n")
        # reset stdout
        sys.stdout = sys.__stdout__

    def test_stdout_inverted_rectangle(self):
        # redirect stdout to a buffer
        sys.stdout = io.StringIO()
        # call the function that should print something
        self.b0 = self.Rectangle(6, 4)
        self.b0.display()
        # get the contents of the buffer
        output = sys.stdout.getvalue()
        # check the contents against expected output
        self.assertEqual(output, "######\n######\n######\n######\n")
        # reset stdout
        sys.stdout = sys.__stdout__


class TestRectangleUpdateattributesNonkeyword(unittest.TestCase):
    """MyClass is an example class for demonstration purposes.

        This class has a single property, `x`, and a single method, `hello()`.

        Attributes:
            x (int): A property that holds a value.

        """

    def setUp(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        self.Rectangle = __import__('models').rectangle.Rectangle

    def tearDown(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        del self.b0
        del self.Rectangle

    def test_that_on_update_values_are_set(self):
        """ Test that on Update expected Values are set"""

        # instantiate Rectangle instance
        self.b0 = self.Rectangle(1, 2, 3, 4, 5)
        self.b0.update(3, 4, 5, 7, 2)

        # verify width update change
        self.assertEqual(self.b0.width, 4)

        # Update height update change
        self.assertEqual(self.b0.height, 5)

        # verify x update change
        self.assertEqual(self.b0.x, 7)

        # verify y update change
        self.assertEqual(self.b0.y, 2)

        # verify id update change
        self.assertEqual(self.b0.id, 3)

    def test_data_value_on_update(self):
        """
        Verifies that parameters are being checked against the allowed data types when update
        class method is invoked
        """
        self.b0 = self.Rectangle(1, 2, 3, 4, 5)
        self.b0.update(3, 4, 5, 7, 2)

        r = self.Rectangle(10, 2)
        with self.assertRaises(ValueError):
            self.b0.update(-3, 4, 5, 7, 2)
        with self.assertRaises(ValueError):
            self.b0.update(3, -4, 5, 7, 2)
        with self.assertRaises(ValueError):
            self.b0.update(3, 4, -5, 7, 2)
        with self.assertRaises(ValueError):
            self.b0.update(3, 4, 5, -7, 2)

    def test_data_type_on_setting(self):
        """
        Verifies that parameters are being checked against the allowed data types
        """
        self.b0 = self.Rectangle(1, 2, 3, 4, 5)
        self.b0.update(3, 4, 5, 7, 2)

        r = self.Rectangle(10, 2)
        with self.assertRaises(TypeError):
            self.b0.update(True, 4, 5, 7, 2)
        with self.assertRaises(TypeError):
            self.b0.update(3, False, 5, 7, 2)
        with self.assertRaises(TypeError):
            self.b0.update(3, 4, False, 7, 2)
        with self.assertRaises(TypeError):
            self.b0.update(3, 4, 5, False, 2)
        with self.assertRaises(TypeError):
            self.b0.update(True, False, True, False, 2)


# todo: complete test cases for the keyword assigning
# Ensure to validate the type and value and verify
# the assigned value
# @unittest.skip("Skipping **kwargs")
class TestRectangleUpdateattributeskeyword(unittest.TestCase):
    """MyClass is an example class for demonstration purposes.

           This class has a single property, `x`, and a single method, `hello()`.

           Attributes:
               x (int): A property that holds a value.

           """

    def setUp(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        self.Rectangle = __import__('models').rectangle.Rectangle

    def tearDown(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        del self.b0
        del self.Rectangle

    def test_that_on_update_values_are_set(self):
        """ Test that on Update expected Values are set"""

        # instantiate Rectangle instance
        self.b0 = self.Rectangle(1, 2, 3, 4, 5)
        self.b0.update(id=3, width=4, height=5, x=7, y=2)

        # verify width update change
        self.assertEqual(self.b0.width, 4)

        # Update height update change
        self.assertEqual(self.b0.height, 5)

        # verify x update change
        self.assertEqual(self.b0.x, 7)

        # verify y update change
        self.assertEqual(self.b0.y, 2)

        # verify id update change
        self.assertEqual(self.b0.id, 3)

    def test_data_value_on_update(self):
        """
        Verifies that parameters are being checked against the allowed data types when update
        class method is invoked
        """
        self.b0 = self.Rectangle(1, 2, 3, 4, 5)
        self.b0.update(3, 4, 5, 7, 2)

        r = self.Rectangle(10, 2)
        with self.assertRaises(ValueError):
            self.b0.update(id=3, width=4, height=5, x=7, y=-2)
        with self.assertRaises(ValueError):
            self.b0.update(id=3, width=-4, height=5, x=7, y=2)
        with self.assertRaises(ValueError):
            self.b0.update(id=3, width=4, height=-5, x=7, y=2)
        with self.assertRaises(ValueError):
            self.b0.update(id=3, width=4, height=5, x=-7, y=2)

    def test_data_type_on_setting(self):
        """
        Verifies that parameters are being checked against the allowed data types
        """
        self.b0 = self.Rectangle(1, 2, 3, 4, 5)
        self.b0.update(id=3, width=4, height=5, x=7, y=2)

        with self.assertRaises(TypeError):
            self.b0.update(id=3, width=True, height=5, x=7, y=-2)
        with self.assertRaises(TypeError):
            self.b0.update(id=3, width=4, height=True, x=7, y=-2)
            self.b0.update(3, False, 5, 7, 2)
        with self.assertRaises(TypeError):
            self.b0.update(id=3, width=4, height=5, x=True, y=-2)
            self.b0.update(3, 4, False, 7, 2)
        with self.assertRaises(TypeError):
            self.b0.update(id=3, width=4, height=5, x=7, y=True)
            self.b0.update(3, 4, 5, False, 2)
        with self.assertRaises(TypeError):
            self.b0.update(id=3, width=True, height=True, x=True, y=True)


class TestRectangleDisplayXnYprint(unittest.TestCase):
    """
    Tests display with x and y taken into account
    """

    def setUp(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        self.Rectangle = __import__('models').rectangle.Rectangle

    def tearDown(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        del self.b0
        del self.Rectangle

    def test_stdout_square(self):
        # redirect stdout to a buffer
        sys.stdout = io.StringIO()
        # call the function that should print something
        self.b0 = self.Rectangle(2, 3, 2, 2)
        self.b0.display()
        # get the contents of the buffer
        output = sys.stdout.getvalue()
        # check the contents against expected output
        self.assertEqual(output, "\n\n  ##\n  ##\n  ##\n")
        # reset stdout
        sys.stdout = sys.__stdout__

    def test_stdout_rectangle(self):
        # redirect stdout to a buffer
        sys.stdout = io.StringIO()
        # call the function that should print something
        self.b0 = self.Rectangle(4, 6, 1, 2)
        self.b0.display()
        # get the contents of the buffer
        output = sys.stdout.getvalue()
        # check the contents against expected output
        self.assertEqual(
            output, "\n\n ####\n ####\n ####\n ####\n ####\n ####\n")
        # reset stdout
        sys.stdout = sys.__stdout__

    def test_stdout_inverted_rectangle(self):
        # redirect stdout to a buffer
        sys.stdout = io.StringIO()
        # call the function that should print something
        self.b0 = self.Rectangle(6, 4, 2, 1)
        self.b0.display()
        # get the contents of the buffer
        output = sys.stdout.getvalue()
        # check the contents against expected output
        self.assertEqual(output, "\n  ######\n  ######\n  ######\n  ######\n")
        # reset stdout
        sys.stdout = sys.__stdout__


@unittest.skip("Not yet Implemented")
class TestRectangleMagicStrMethod(unittest.TestCase):
    pass


@unittest.skip("Not yet Implemented")
class TestRectangleToDictionary(unittest.TestCase):
    pass


if __name__ == "__main__":
    """
    Groups multiple testcase Classes into a suite
            """
    suite_loader = unittest.TestLoader()
    suite1 = suite_loader.loadTestsFromTestCase(TestRectangle)
    suite2 = suite_loader.loadTestsFromTestCase(TestRectangleArea)
    suite3 = suite_loader.loadTestsFromTestCase(TestRectangleDisplay)
    suite4 = suite_loader.loadTestsFromTestCase(TestRectangleDisplayXnYprint)
    suite = unittest.TestSuite([suite1, suite2, suite3, suite4])
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
