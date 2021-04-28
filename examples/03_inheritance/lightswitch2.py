
class LightSwitch:
	am_i_on = True

	def toggle(self):
		self.am_i_on = not self.am_i_on

	def sayState(self):
		if self.am_i_on:
			print("I am on!")
		else:
			print("I am off!")


class DimmerSwitch(LightSwitch):
	brightness = 0

	def increaseBrightness(self):
		self.brightness += 1

	def decreaseBrightness(self):
		self.brightness -= 1

	def sayState(self):
		if self.am_i_on:
			print("I am on! Brightness: {}".format(self.brightness))
		else:
			print("I am off!")
