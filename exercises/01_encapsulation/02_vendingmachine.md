# Vending Machine
In this exercise, we'll create a class that has a few more moving parts. Let's consider a vending machine that lets us; stock the machine with items (setting a name, price, and quantity), pay for items, and print out the current stock. 

An example interaction with an instance of this class should look like this;

```bash
>>> import vendingmachine as vm
>>> initial_stock = [('oreos', 2, 10), ('m&ms', 1, 10)]
>>> machine = vm.VendingMachine('My Machine', initial_stock)
>>> machine.showStock()
Machine: My Machine
oreos -     2$ - 10
m&ms  -     1$ - 10
>>> machine.addCoins(3)
added 3 coins, 3 currently inserted.
>>> machine.purchase('oreos')
Have a oreos!
>>> machine.purchase('oreos')
Need 1 more coins!
>>> machine.purchase('m&ms')
Have a m&ms!
>>> machine.showStock()
Machine: My Machine
oreos -     2$ - 9 
m&ms  -     1$ - 9 
>>> machine.showCoins()
Machine: My Machine
Current bank: 3
Current coins inserted: 0
```

The machine should also be able to handle some 'stocking operations'. These could probably be done in some more elegant, combined method, which we'll leave as an additional exercise. However, we'll keep it simple and use two stocking methods; one for an existing item, and one for a totally new item;

```bash
>>> machine.restockItem('oreos', 20)
>>> machine.showStock()
Machine: My Machine
oreos -     2$ - 29
m&ms  -     1$ - 9 
>>> machine.addItem('pizza', 5, 10)
Added pizza
>>> machine.showStock()
Machine: My Machine
oreos -     2$ - 29
m&ms  -     1$ - 9 
pizza -     5$ - 10
```

To get you started, there is a template file, vendingmachine.py, that contains method stubs and reminders of what state each should be modifying and how. 

## Suggested Python Skills
* Dictionaries
* Format Strings

