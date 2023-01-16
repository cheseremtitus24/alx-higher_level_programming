#!/usr/bin/python3
import unittest


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
        These are module setUp
        Teardown Methods
        :return:
        """
        pass

    @unittest.skip("Not yet implemented")
    def test_from_json_string(json_string):
        """
        These are module setUp
        Teardown Methods
        :return:
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
