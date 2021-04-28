# OOP In the Wild
Before moving onto the other topics, I'd like to show how object oriented programming is a common choice for organizing frameworks. As an example, lets look at a library that has us create instances of simple obejcts, and interact with them to make things happen. In the future, we will look at libraries where we use more complex OOP principles to interact with them. For instance, some more 'heavy weight' frameworks, like GUI (Graphic User Interface) frameworks, use inheritance, and have the user create classes that are an extension of a base class.  

For now we'll stay simple, and deal with ones that provide us classes that we can make interesting Objects out of. 

# synthesizer
[Synthesizer](https://pypi.org/project/synthesizer/) is a simple python library for creating noises. That link should provide enough information to get the dependencies and library installed. But the crib notes are;

```shell
../examples/02_oop_in_the_wild$ sudo apt install portaudio19-dev
../examples/02_oop_in_the_wild$ pip3 install pyaudio
../examples/02_oop_in_the_wild$ pip3 install synthesizer
```
You may need to use 'pip' vs 'pip3'.

## Basics
Once we have the library installed, we can start a REPL to interact with it. 

```shell
# examples/02_oop_in_the_wild
>>> from synthesizer import Player, Synthesizer, Waveform
```

In our first line, we see that we're importing three specific class files from the synthesizer library. We'll see how we use these imports to create instances of the Classes they represent. This code is ripped directly from the examples provided in the synthesizer frameworks documentation, [here]()

```shell
>>> player = Player()
>>> player.open_stream()
>>> synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
>>> chord = ["C3", "E3", "G3"]
>>> player.play_wave(synthesizer.generate_chord(chord, 3.0))
```

If you run the above, you might see a bunch of log output telling you a bunch of information about ASLA lib or other weird stuff. Ignore it. You SHOULD hear a chord being played. 

We see classes being created twice. On the first line, we see a Player class being instantiated and a reference stored to it in 'player'. On the third line, we create an instance of a Synthesizer.

Our third class file (Waveform) isn't used to create an instance of a class, but is instead being used as a convient way to access methods that are being organized in some helpful way. Waveform is a class, but it is providing access to what we could call 'static methods of that class'. This shows us that a class file can contain more than just the definition of a class. Many times, a class file also contains other methods that are useful in the contexts in which the class is typically used. These are not methods that are defined 'on' or 'within' the class definition itself, but rather ones defined outside of it that are very related to the class's function, but ones that do not make sense to attach to an 'instance' of that class.

In the line in which we create the Synthesizer object, we see that one of the possible named parameters takes a 'Waveform' 'function'. According to the documentation, this is a function that maps a time step to an output intensity, otherwise known as a 'waveform'. The Waveform class contains many 'static methods' that behave like waveforms! One such function is the 'sine wave', which we access 'through' the class file as seen in the example. 

Now I don't know much about music, but now I know that if I can find a set of those strings representing notes that I like, I can package them up like that, and have this code play it for me.  Neat. 

TODO - Add refernces to the doc for Waveform, and the Syhtesizer constructor.

## Data Hiding
One thing I'd like to point out about this example is that it highlights one of the more nuanced aspects or goals of encapsulation; data hiding. As we mentioned at the end of _01_, creating a Class should be an exercise in protecting the user from shooting themselves in the foot, by ensuring that the only way to mess with the state of an object of a particular class, is through the methods you define on it. 

We have a very complex notion of a 'Music Player', all encapsulated by the class Player. As the user of the Class, I don't need to know about the particulars of interacting with the hardware on my machine that makes noise. This class does all that behind the scenes, and presents me, the user, with a small set of methods that let me interact with that complex code base. 

TODO - Discuss details of what open_stream() doesn.
TODO - Link to the doc/source for it. 

We see this again in the Synthesizer class. Also, we see that this class has a constructor that allows for 'named parameters' that handle some configuration options. 

TODO - Discuss that final line. Make sure they see that its a call to one object, then a call to a second object, using the result of the first call as the parameter for the second. 
