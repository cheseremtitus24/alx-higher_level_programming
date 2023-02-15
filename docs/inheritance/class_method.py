
class Pet:
	_class_info = "pet animals"

	@classmethod
	def about(cls):
		print("This class is about " + cls._class_info + "!")
class Dog(Pet):
	_class_info = "man's best friends"
	
class Cat(Pet):
	_class_info = "all kinds of cats"


Pet.about()
# This class is about pet animals!
Dog.about()
# This class is about man's best friends!
Cat.about()
# This class is about all kinds of cats!

