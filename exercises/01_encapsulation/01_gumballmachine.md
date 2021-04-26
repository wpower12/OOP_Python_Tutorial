# Gumball Machine
In this exercise you'll create a class that represents a simple gumball machine. You'll make a gumballmachine that has as its state a color and an initial quantity of gumballs. To keep things simple, we'll assume gumballs always cost a quarter, and that you only have to do two things to get a gumball out of the machine; put a quarter in the slot (putQuarter()) and turn the handle (turn()).

An example interaction with your machine in the REPL should look like this:

```bash
>>> import gumballmachine as gbm 
>>> redgbm = gbm.GumBallMachine('red', 2)
>>> redgbm.putQuarter()
>>> redgbm.turn()
have a red gumball 
>>> redgbm.turn()
no quarter in slot!
>>> redgbm.putQuarter()
>>> redgbm.putQuarter()
Jam! Already a quarter in the slot!! Ouch!
>>> redgbm.turn()
have a red gumball 
>>> redgbm.putQuarter()
>>> redgbm.turn()
Out of gumballs!!
```

To get you started, there is a template file with the method names written out, and reminders of what each method should accomplish in the gumballmachine.py file. 

## Suggested Python Skills

* Booleans
* Boolean Expressions
* String Formatting