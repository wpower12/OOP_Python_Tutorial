# Encapsulation
To help us talk about this topic more clearly, I'd like to begin by explicitly defining a term; State. You may have already seen this word used as part of a definition of an Object or Class. We use Objects to help us manage the state of some thing. 

## State
Lets start with some examples. Consider the humble light switch. We can easily talk about its state, and it seems trivial to enumerate the possible states. A lightswitch can be on, or it can be off. When we talk about a specific lightswith, that is, one we've bought, purchased, and connected to an existing electrical circuit, we can say then (usually) say which of these two states the lightswitch must be 'In'. 

To use the langauge of OOP; "when we make an object, we can make assumptions about its state, based on how we defined the object". 

## Classes and Class Basics
Before we continue with the definition of encapsulation, it might be useful to see how we use the paradigm of Object Oriented Programming in or with a specific programming language.  Different programming langauges have different techniques to manage the 'bookkeeping' of objects. That is, what methods and procedures do we use to create objects and interact with them? 

Many languages use the notion of a 'class' to represent an Object. So many, that it is easy to simply use the terms Object and Class interchangeably. I'll be pedantic and try to keep the separation between the abstract notion of an Object, and the specific implementation of them; Classes. 

The language python (which I'll be using for most of the examples) uses the following syntax to create a class (its implementation of an Object). To show the syntax off, lets use the example of the light switch, our simple 2 state object. 

TODO:AddReferencesToPythonDocs

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
```

I'm going to gloss over a bunch of details, and instead jump to an example of how we go on to use this class definition to actually CREATE an object. If we start a REPL in our example directory, we can IMPORT the file containing our class to try and use it. 

```bash
>>> import lightswitch as ls
>>> switch = ls.LightSwitch()
```

While the LightSwitch class is an abstract definition OF a light switch, we now have an actual INSTANCE of the LightSwitch class. We can refer to switch as an "object" who is of the class (in typed languages it might even make sense to say 'type') LightSwitch. We refer to this process as 'instantiating a class'. We are making a specific, discrete, usable INSTANCE of the object we defined. 

Now that we have an instance of the object, we can interact with it! The class definition says that we have two METHODS avaialable to us; toggle and sayState. To use them, we interact with our instance of the object like so;

```bash
>>> switch.sayState()
I am on!
>>> switch.toggle()
>>> switch.sayState()
I am off!
```

You might hear this referred to as "calling a method defined on an object". We say "defined on" to refer to the fact that these methods are part of our abstract definition of the Object. We 'call' them by telling python which object we are referring to, then a dot, then the name of the method defined ON the object.

It is important to make clear that there can be many instances of any given class or object, and that each one is managing its own state. Consider adding another switch;

```bash
>>> other_switch = LightSwitch()
>>> switch.sayState()
I am off!  
>>> other_switch = LightSwitch()
>>> other_switch.sayState()
I am on!
```

## Class Components
In our lightswitch example, we can see that there are roughly two 'kinds' of things that make up a class. We have a set of variables (the am_i_on variable for instance) specific to the object, and we have functions that operate on these. In OOP parlance, we refer to these as fields and methods. 

Fields are the variables that hold a class' state. You might be wondering; 'how does an object get an initial state?'. We can see one way in the light switch example; simply assinging a value to field in the class definition. However, we might want to specify some inital state when we create (aka 'instantiate') an object. 

To do this, we can write a special kind of method on our class called a 'constructor'. Constructors are (unsurpsingly) responsible for constructing a new instance of an object. This method is the place where you'd want to provide any intial configuration or state values for your new instance. 

To show this off, lets consider a slightly more involved example, perhaps a new Character in a RPG. The following shows a possible class definition for a Character, highlighting the syntax python uses for writing a constructor; '__init__'

```python
class Character:

    def __init__(self, p_name, p_class, max_health):
        self.player_name  = p_name
        self.player_class = p_class 
        self.max_hp       = max_health
        self.current_hp   = max_health

    def whoAreYou(self):
        print("I am {}, a {}".format(self.player_name, self.player_class))

    def hurt(self, dmg):
        self.current_hp -= dmg
        if self.current_hp <= 0:
            print("I\'m dead!")

```

As we see above, the special method "__init__" allows us to write a constructor for our class. It's now important to call out the 'self' keyword. In python, this is used to represent the state of a particular instance of the class. That is, when we write methods (even the constructor) on a class, we use the self keyword to get access to the current values of the instances fields, at the time the method is called. 

This keyword is very important in the constructor definition. This is how we 'save' our actual initial state. We access the classes fields through the self keyword, and assign them new values.

We can see our methods and constructor in action in the REPL:

```bash
>>> import character as c 
>>> bob = c.Character("Bob", "Mage", 20)
>>> bob.whoAreYou()
I am Bob, a Mage
>>> bob.hurt(20)
I\'m dead!
```

## Overview
These examples barely scratch the surface of the concept of encapsulation, but they should provide a good starting point for the rest of this content. Hopefully it's now easy to see how Objects can be used to create useful, manageable abstractions of a large variety of things. 

As an initial exercise, consider some more methods you could add onto the Character class. Perhaps some that have different outputs based on the class of the character. 

Additionally, there are more concrete exercises provided in the  '/exercises/01_encapsulation' directory. 