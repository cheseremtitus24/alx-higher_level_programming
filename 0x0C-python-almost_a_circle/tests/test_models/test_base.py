#!/usr/bin/python3
import unittest
import io
import sys


class TestBase(unittest.TestCase):
    def setUp(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        self.Base = __import__('models').base.Base

    def tearDown(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        del self.b0
        del self.Base

    def test_id_autogen(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        # id is a positive number
        self.b0 = self.Base(3)
        self.assertEqual(self.b0.id, 3)

        # id is zero
        self.b0 = self.Base(0)
        self.assertEqual(self.b0.id, 1)

        # id is negative
        self.b0 = self.Base(-1)
        self.assertEqual(self.b0.id, 2)

        # id is a non integer
        self.b0 = self.Base(True)
        self.assertEqual(self.b0.id, 3)


    @unittest.skip("Not yet implemented")
    def test_save_to_file(cls, list_objs):
        """
        dumps a list of dictionaries and serializes them
        into a json string
        :return: a json string of a list of dictionaries
        """

        pass

    @unittest.skip("Not yet implemented")
    def test_to_json_string(self):
        """
        Tests that contents of a dictionary are
        serialized into a json string and that
        the string is returned
        """
        self.b0 = self.Rectangle(10, 7, 2, 8)
        dictionary = self.b0.to_dictionary()
        json_dictionary = self.b0.to_json_string([dictionary])
        # redirect stdout to a buffer
        sys.stdout = io.StringIO()
        # call the function that should print something
        print(json_dictionary)
        # get the contents of the buffer
        output = sys.stdout.getvalue()
        # check the contents against expected output
        self.assertEqual(output, "[{\"x\": 2, \"width\": 10, \"id\": 1, \"height\": 7, \"y\": 8}]\n")
        # reset stdout
        sys.stdout = sys.__stdout__

    @unittest.skip("Not yet implemented")
    def test_from_json_string(json_string):
        """
        
        """
        pass

    @unittest.skip("Not yet implemented")
    def test_create(cls, **dictionary):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        pass


if __name__ == "__main__":
    unittest.main()
