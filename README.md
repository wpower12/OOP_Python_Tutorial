# Object Oriented Programming with Python
This is a short(?) tutorial on the topic of Object Oriented Programming; what it is, why we use it, how we use it, and examples of its use 'in the wild'.

## Goals of OOP
When we program, our task is to translate some real problem in the world to the language of a computer, such that we find a solution to said problem. In the service of this, we create a file, or usually many files. These are organized in a way that their contents and logical abstractions can be shared and used between eachother. Programming is largely about managing this mass of possibly-pasta-like complexity.

To help us manage this complexity, a variety of paradigms and frameworks have been developed to help us make choices about how to organize code while solving problems. Object Oriented Programming is one such paradigm. It attempts to help wrangle the complexity beast by considering code as a collection of Objects that represent abstractions of the parts, or the whole, of the problem at hand. These Objects can interact with each other, behaving as 'clients' of each others code. 

The core idea is that we can define a Class, representing an Object in the abstract, that contains data and methods to operate on that data. 

There are many components to OOP, and different languages will provide built-in help for a variety of subsets of the full world of OOP features and concepts. To keep it simple, I'll focus on a few core ideas. I think these represent a minimal set to begin using OOP concepts 'in the wild', that is to interact with frameworks and organize personal projects. 

The main concepts I'll be focusing on will be;

* Encapsulation - How we organize a Class representing a single abstraction.
* Inheritance/Polymorphism - How we organize a hierarchy of abstractions, and how and when we can use one Class as if it were another. 

This tutorial will attmept to work through these topics, presenting discussion and exercises along the way. 

## Structure
The top level directory contains markdown files with discussion content. Any exercises mentioned will have template files and problem descriptions within directories inside the exercies folder. Answers to said exercises are also provided in the solutions directory. 

I'll be writing these discussion documents assuming you have a terminal open to the directory, and can navigate to the relvant directores for each topic. Some discussions will reference example code that can be imported into the python REPL so you can 'play along' with the code examples. To make imports easier, start your REPL in the same scope as a the example code. I'll write the example code assuming thats where you started. 

I'll be using python3 for this. Sorry Nick. 

## Next
[Encapsulation](01_Encapsulation.md)