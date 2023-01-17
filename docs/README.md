class methods make use of the decorator @classmethod
and usually have the first parameter as (cls) which reference to an 
object instance.

## class Methods and instance method in inheritance.

We define a class **Pet** with a method **about**.
This method should give some general class information.

The class **Dog** and **Cat** are subclasses/children of the **Pet** class.

Below shows the method **about** being inherited as an **instance method**


***
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


***

This may look alright at first glance. On ***second thought we recognize the awful design*** 
** NOTE: We had to create instances of the Pet, Dog and Cat classes to be able to ask what the class is about**

### it could be alot better if we could just write
***
Pet.about()
Dog.about()
Cat.about()
***

#### Using Class Methods makes the Latter Possible

***
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

***

	


