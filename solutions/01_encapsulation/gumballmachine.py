class GumBallMachine:

	def __init__(self, c, q):
		self.color = c
		self.quantity = q
		self.have_quarter = False

	def putQuarter(self):
		if self.have_quarter:
			print("Jam! Already have a quarter")
		else:
			self.have_quarter = True

	def turn(self):
		if self.have_quarter:
			if self.quantity > 0:
				print("have a {} gumball".format(self.color))
				self.quantity -= 1
				self.have_quarter = False
			else:
				print("out of gumballs!")
				self.have_quarter = False # Give it back.
		else:
			print("No quarter! Nothing happens!")

