class Person:
	name = 'Anonymous';

	def setName(self, newName):
		self.name = newName

	def printYourName(self):
		print "My name is: " + self.name

	def writeYourSpecialTraits(self):
		print "... Nothing ..."

class SuperHero(Person):
	def __init__(self):
		self.specialTrait = 'No super hero traits yet'

	def setSpecialTraits(self, specialTrait):
		self.specialTrait = specialTrait

	def writeYourSpecialTraits(self):
		print "My spcial trait is: " + self.specialTrait

superMan = SuperHero()

superMan.writeYourSpecialTraits()
superMan.setSpecialTraits("I can fly")
superMan.writeYourSpecialTraits()
