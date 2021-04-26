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
	coin_buffer = 0
	name = ""

	def __init__(self, name, initial_inventory):
		self.name = name

		for item in initial_inventory:
			# 'Variable Unpacking', some syntactic sugar.
			item_name, item_cost, item_amt = item

			# We'll use the name of the item as its key.
			# The value will be a 'tuple' containing the
			# cost of the item, and the amount we have in
			# stock. 
			self.inventory[item_name] = (item_cost, item_amt)

	def showStock(self):
		print("Machine: {}".format(self.name))
		# When we use these 'enhanced' for loops with a dict,
		# the items we are given as we 'iterate' are the KEYS
		# of the dict. So in this case, we are actually iterating
		# over all the item NAMES in the dict.
		for item_name in self.inventory:
			# More unpacking! Recall, the KEYS of our dict()
			# are item names, see the constructor where we used
			# that to 'fill in' an entry in the dict? 
			cost, qty = self.inventory[item_name]
			print("{:<5} - {:>5}$ - {:<2}".format(item_name, cost, qty))

	def showCoins(self):
		print("Machine: {}".format(self.name))
		print("Current bank: {}".format(self.bank))
		print("Current coins inserted: {}".format(self.coin_buffer))

	def addCoins(self, coins):
		self.coin_buffer += coins
		print("added {} coins, {} currently inserted.".format(coins, self.coin_buffer))

	def purchase(self, item):
		# We need to handle the two possibilities for the item
		# if 'item' is a key in our self.inventory dict, or if
		# 'item' is NOT a key. We can use some of the dictonary methods
		# to do this. Otherwise, we would get an 'exception' when trying
		# to find a key that does not exist. 
		if item in self.inventory:
			cost, qty = self.inventory[item]

			# We can only purchase if there are a non-0 
			# number of the thing left, and if the user has
			# put in enough coins. Booleans!
			if (qty > 0) and (self.coin_buffer >= cost):
				print("Have a {}!".format(item))
				# We have to update our inventory to reflect 
				# the sale. So we 'overwrite' the contents
				# of the dict. 
				self.inventory[item] = (cost, qty-1)
				# Then we update the state of our coins. 
				self.coin_buffer -= cost
				self.bank += cost
			
			else:
				# here we handle the other two possible 'errors'
				if qty == 0:
					print("Out of {}! Need to restock!".format(item))

				if self.coin_buffer < cost:
					print("Need {} more coins!".format(cost-self.coin_buffer))

		else:
			print("Item not in stock! Ask your supplier to add {}".format(item))

	def restockItem(self, item, amount):
		# Should handle 
		if item in self.inventory:
			cost, qty = self.inventory[item]
			self.inventory[item] = (cost, qty+amount)
		else:
			print("item {} not found!".format(item))

	def addItem(self, item, cost, qty):
		self.inventory[item] = (cost, qty)
		print("Added {}".format(item))

