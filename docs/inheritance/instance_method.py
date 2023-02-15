
class Pet:
	# _class_info is a protected class attribute that is 
	# made accessible to child classes

	_class_info = "pet animals"
	
	def about(self):
		print("This class is about " + self._class_info + "!")
class Dog(Pet):
	_class_info = "man's best friends"
class Cat(Pet):
	_class_info = "all kinds of cats"

p = Pet()
p.about()
# This class is about pet animals!
d = Dog()
d.about()
# This class is about man's best friends!
c = Cat()
c.about()
# This class is about all kinds of cats!


