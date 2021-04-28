##
# vendingmachine.py
##
class VendingMachine:
	# You could leave these off and define them all in the
	# constructor, but I'll leave them here to just be
	# explicit. You'll see patterns like this more often in
	# languages like Java/C. Python is more flexible?
	inventory = dict()
	bank  = 0
	coin_buffer = 0 # The number of coins currently inserted.
	name = ""

	def __init__(self, name, initial_inventory):
		# We'll want to set out name, and then use the
		# LIST 'initial_inventory' to fill in the 
		# elements of our DICT: self.inventory.
		# Hint: Dicts are sequences that we can iterate over
		# in a for loop, the value we get at each iteration
		# is one of the KEYS in the dict. 

	def showStock(self):
		# iterate over our inventory and display the items
		# some google terms: 'python format strings alignment'
		# Hint: Remember, when we iterate over a DICT we are
		# 'looping through' all of its KEYS


	def showCoins(self):
		# Report our cash moneys.

	def addCoins(self, coins):


	def purchase(self, item):
		# You'll want to handle if the item is a key or not,
		# otherwise you'll get exceptions when it isnt.


	def restockItem(self, item, amount):
		# add more of an existing item
		# We could maybe handle these two methods
		# in some combined, elegant way, but this
		# works for now. 
		# HINT: The 'in' keyword works with DICTs 
		# to check if 'KEY in DICT'. 


	def addItem(self, item, cost, qty):
		# Add a totally new item. Note we
		# have a 'cost' parameter now, compared
		# to the restock method, where we didnt. 


