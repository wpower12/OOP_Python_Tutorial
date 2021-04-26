# More OOP In the Wild
Now that we have a basic udnerstanding of Inheritance, we can look at those more 'heavy weight' frameworks mentioned earlier. 

# TKinter 
The Library TKinter provides tools to help a programmer Graphical User Interfaces (GUIs). To do this, TKinter has the programmer define a class that Inherits from a base class, responsible for defining all the required methods for the object to behave like a proper, rendered screen that a user can interact with. 

TODO - how to install Tkinter
For Ubuntu:

```shell
$ sudo apt-get install python3-tk
```

[link](https://tkdocs.com/tutorial/install.html#installlinux)

TODO - Links to TKinter docs


## Example GUI App Class
The following is a minimum example of creating our class the extends the Frame class provided by the tkinter library. The Frame is a class representing a collection of application elements. It lets us isntantiate and configure other classes, like the 'tk.Button' class.  This code comes from the examples in the documentation, found [here](https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program)

```python
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
```

To see this in action, we can navigater to the 04 examples directory and run;
```shell
../examples/04_more_oop_in_the_wild$ python3 basicgui.py
```

If everything is installed and we python points the a python3 binary, then you should see a tkinter application windo appear, with a 'hello world' Button, and a 'quit' Button. 

TODO - More of an explanation. 