# Inheritance
We've talked about how OOP is a technique for helping us cope with complexity. Our first concept, Encapsulation, showed us one facet of this. We learned the syntax for class creation and instantation, along with some guidelines about how we should organize and use the two elements of a class; fields and methods. The examples in 02 should be a nice way to see this in action, particularly the idea of 'data hiding'. 

The idea of an abstract Object is more than just a way to 'contain' data and methods. When we speak of Objects in the 'real world', we usually do so in some natural hierarchy; "cat" is a kinda of "animal", "truck is a kind of car", "Whole Numbers are a kind of Integer". This relationship 'a kind of' is also an important concept that we can establish with Object Oriented Programming. This is useful because it lets us do more than just organize fields and methods, it lets us organize how the larger set of classes in our program interact. It lets us make more or less 'specific' kinds of classes out of another.

## Lightswitch Revisted
Lets just jump into an example. Lets take our old friend 'lightswitch'. In the original lightswitch, our state was simple, we had to track 'am_i_on'. Lets say you just figured out that dimming is cool, and want to make a new LightSwitch class that can handle some notion of this, perhaps a new LightSwitch that also track some 'brightness' value, as well as 'am_i_on'

Now, we know we have our toggle logic down. So we wont change that. All we'd like to do is track a brightness, and add some ability to increase or decrease this brightness. In other words, we want to keep some of the structure of LightSwitch, but add a little bit of extra functionality to make a DimmerSwitch out of it. 

This is the process and purpose of inheritance! It lets us tell a programming language that a particular class 'inherits' from another, and we'd like to 'start off' with that class, and modify it in some way. To do this in python, we can take a look in the '03_inheritance' example directory, at a new lightswitch2 class. 

```python
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
```

The first part of the file just repeats the 'base class' we want to inherit from; LightSwitch. Then, in our second class definition, we can see the syntax for python Inheritance. When we add a set of parens, with the name of a class inside of them, to the 'declaration' of a class, we are telling python which class to inherit from. In this instance, we are telling python that this class we are writing, DimmerSwitch, should inherit all of the fields and methods that we defined in the original LightSwitch class. 

After we do that, we do the same thing to create a DimmerSwitch. All the other patterns we've learned for objects and classes will also apply to our dimmer switch. To be explicit, open up a REPL and instantiate some objects!

TODO - Example REPL Interaction

An important thing to point out here is that we did NOT have to write a toggle method when we wrote our DimmerSwitch. Since we 'started with' all of the components of a LightSwitch, that was already available to us! But wait, you say, what about that 'new' sayState method?

We can choose to 'reimplement' an existing method of a class we inherit from. This is known as '__method overwriting__'. We choose to make a 'more specific' version of our sayState method, one that we know will handle our additional state now that the LightSwitch class has had more state added to it by the DimmerSwitch class. 

## Polymorphism
The idea of inheritance gives OOP the flexibility of a 'kind-of' relationship. An additional benefit of this relationship is that it lets us encode an idea of 'when can I do what to what?' into our programs. In other words, a hierarchy of class definitions implies there are 'equivalant sets' of classes. We can decide to treat some part of the hierarcy as if they were all the most base class, to simplify writing some part of our code. 

Lets go back to our RPG characters. In an RPG there are lots of "Character" like things. Not just the player characters, but the characters you meet along the way, the NPCs, and the enemy characters. It might make sense to keep a base 'Character' class that does all the basic things all of these 'types' of character have in common, and then 'inherit' from that class to create other, specialized kinds of character. Note, there are lots of ways to decide on a class hierarchy, what follows is one posibility. Try others!

Lets say our base character assumes that any 'entity' we want to 'model' with a Character class is going the: have health (hp), have a name, and an inventroy. All characters will have 'takeDamage', 'healDamage', 'giveItem' and 'checkInventory' methods.

```python
class Character:
    name   = "Defaultio"
    health = 10
    inventory = []

    def __init__(self, n, h):
        self.name   = n 
        self.health = h

    def takeDamage(self, dmg):
        self.health -= dmg

    def healDamage(self, dmg):
        self.health += dmg

    def giveItem(self, item):
        self.inventory.append(item)

    def checkInventory(self):
        print("{} has:".format(self.name))
        for i in self.inventory:
            print(" - {}".format(i))
```

These seem like good, basic things you'd want all your characters to be able to do. Remember, we want to __Encapsulate__ our data and logic so we interact with our class in a reasonable sequence of method calls to modify its internal state. These methods make sense for our purposes, as they allow us to modify the things that seem to 'make sense' to be modifiable. We're assuming (or indicating, or deciding), the name field shouldn't be modifiable after we call the constructor to instantiate a class into an object. 

Now, we might want to handle other classes. Maybe we want to handle some classes that do more than this, perhaps some that make 'attacks' and track how powerful it is. Maybe we'd like to have spells for a wizard, and be able to track which ones they've made ready for an encounter (sorry to non-DnD folks.)

To create more complex 'kinds of' Character, we can Inherit from it, while adding this additional functionality.

In our 'problem context', lets assume that were creating these programmatic representations of characters simply because we want an easy way to track the results of things like attacks and heals. Different characters will be able to do one or the other, and their 'stats' will affect the outcome of some random chance roll. 

So when we have classes that represent entities that can attack or heal, it would make sense that when we write their 'attack' or 'heal' methods, the job of those methods would be to 'roll the dice' based on the 'stats' of the character whose method is being called. 

Lets take the Brawler for an example 'extension' to the Character class. We're going to assume that all a Brawler does is hit things. It has a simple 'hit' method that rolls a random die from 

```python
import random

class Brawler(Character):
    attack_power = 0

    def __init__(self, n, h, p):
        super().__init__(n, h)
        self.attack_power = p

    # Returns the 'result' of a 'hit' from the Brawlers 
    # mighty fists. 
    def hit(self):
        dice_roll = random.randint(0, self.attack_power)
        return dice_roll

```

TODO - Explanation of super()

TODO - Example interaction. 