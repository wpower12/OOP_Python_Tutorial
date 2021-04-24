##
# lightswitch.py
##
class LightSwitch:
	am_i_on = True

	def toggle(self):
		self.am_i_on = not self.am_i_on

	def sayState(self):
		if self.am_i_on:
			print("I am on!")
		else:
			print("I am off!")
