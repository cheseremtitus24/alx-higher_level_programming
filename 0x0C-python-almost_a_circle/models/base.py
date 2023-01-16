import json
"""
This module contains the base class
of a set of inherited classes.
It is responsible for autogenerating the
unique id's of each created object
"""


class Base:
    """ This class represent the base class
    and contains an initialization instance method
    that autogenerates instance number id's of
    class objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is an initialization instance method
        that autogenerates instance object's ids
        and takes in a single parameters that
        accept integers.
        It also takes in a default value of None
        """
        if (type(id) in [int] and id > 0):
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def to_json_string(list_dictionaries):
        """
        dumps a list of dictionaries and serializes them
        into a json string
        :return: a json string of a list of dictionaries
        """
        return json.dumps(list_dictionaries, sort_keys=False)

    @classmethod
    def save_to_file(cls, list_objs):
        """Adds write rectangle objects to a file

                    Args:
                         cls : The class reference passed in
                         list_objs (list(cls_objs))): list of class objects

                """

        fname = cls.__name__
        # print(fname)
        # print(list_objs)
        result = list()
        if not list_objs:
            fp = open(f"{fname}.json", mode='w', encoding='utf-8')
            fp.write("[]")
            fp.close()
            return
        for item in list_objs:
            result.append(item.to_dictionary())
        data = cls.to_json_string(result)
        # print(cls.to_json_string(list_objs[0]))
        fp = open(f"{fname}.json", mode='w', encoding='utf-8')
        fp.write(data)
        fp.close()

    @staticmethod
    def from_json_string(json_string):
        """deserializes a list of string
        class to return a list of class objects

                    Args:
                         json_string (str): a string
                         containing class dictionary objects

                    Returns:
                         class list
                """
        json_object = json.loads(json_string)
        return json_object

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_rect = cls(0, 0, 0, 0, 0)
        else:
            dummy_rect = cls(0, 0, 0, 0)
        dummy_rect.update(**dictionary)
        return dummy_rect

    @classmethod
    def load_from_file(cls):
        fname = cls.__name__
        try:
            fp = open(f"{fname}.json", mode="r", encoding="utf-8")
            contents = fp.read()
            fp.close()
        except BaseException:
            return "[]"
        else:
            item_class_list = cls.from_json_string(contents)
            retval = list()
            for item in item_class_list:
                retval.append(cls.create(**item))

            return retval
