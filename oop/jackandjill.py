class Person:
	name = 'Anonymous';

	def setName(self, newName):
		self.name = newName

	def printYourName(self):
		print "My name is: " + self.name


jack = Person()
jack.setName("Jack")

jill = Person()
jill.setName("Jill")

jack.printYourName()
jill.printYourName()
