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
The idea behind this repository is that you can read the markdown files as tutorials, while interacting with example code in a terminal at the same time. When examples are shown, they'll typically be of either actual python code, expressions written into a REPL, or commands written into a shell (your terminal). 

### REPLs
For those who maybe haven't seen this term yet, a Read-Eval-Print-Loop program is a special program, similar to a shell, that reads in lines of expressions, and evaluates them. It then prints the result of this expression, and the sits looping, waiting for the next expression.

This pattern is pretty common, so it gets the short hand name. Many langauges ship with a REPL in which you can write statements in that language into the REPL program, and see how it would be interpreted by that language. 

Python is one such language. You can invoke the 'Python REPL' in a shell by simply typing 'python'. You should see your prompt spit out some nice notices about what version python you're using, and then change your prompt to a: 

```shell
>>>
```

### Helpful Patterns
When I drop into a REPL during a specific tutorial, I'll write a line at the top that says which directory (relative to the top level directory of the project) I am in when I started that REPL session. For example, if you're reading the 01 tutorial, and see a block like:

```shell
# examples/01_encapuslation/
>>> print("hello from inside 'examples/01_encapuslation!'")
```
You'll know where you need to cd to in order to be in the same place when you start the REPL. This is important because many exmaples will assume you are in this location wehn we import the example code files, or call a specific python script. 

You're encouraged to tweak and tinker on all the provided example code to see what happens! Just know that when you make changes to the source code, you'll need to restart your REPL and reimport the changed files to see the updates you've made. 

When there's an example of an interaction just in the shell, I'll append the relative directory in front of the terminal prompt as a reminder of where you should be to run the same code. 

```shell
../examples/01_encapsulation$ echo "Hi!"
```

### Exercises
Each tutorial file will have related exercises found in the exercises directory. When there are multiple exercises, they'll be ordered in some kind of increasing-difficulty order. Each will come with an empty file to get you started. These usually just contain method stubs with reminders of your goals. Each exercise has a corresponding solution file in the corresponding solution directory. 

## Next
[Encapsulation](01_encapsulation.md)