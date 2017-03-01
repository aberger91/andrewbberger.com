<div id='title'> Teach Yourself Computer Programming </div>
    Andrew Berger Jan. 25, 2017

<div id='text'>
This article is meant for anybody and everybody who has always wanted to learn how to write computer programs, but has not had the time or motivation or whathaveyou.

Before I learned how to write code, computer programming was a strange place I could never quite 
wrap my head around. Even now some things still boggle my mind. But Python makes everythang more better!
</div>
***

##Start with Python
<div id='text'>
If you are like me and had little to no programming experience prior to reading this, I recommend learning Python as a first language.
While Python's level of abstraction compared to other languages like Java or C may not be as informative to the novice programmer (you don't have to declare variables or even think about types at all), I would still advocate to learn Python first. Here's why.
***

Intuitive syntax and indentation leads to clean, readable code.
That's not to say you can't write awful, disgusting looking code in Python (I've been guilty too), but forcing indentation for scope and syntax usually makes reading the code easier for people who haven't read code before. For example:
</div>

    :::c
    #include <stdio.h>
  
    int main(int argc, char** argv)
    {
        if (argc >= 1)
        {
            char* s = argv[1];
            printf("Hey, %s!", s);
        }
        return 0;
    }
***

<div id='text'>
You could find the above code written like so:
</div>

    :::c
    #include <stdio.h>
  
    int main(int argc, char** argv)
    { if (argc >= 1)
    { char* s = argv[1]; 
       printf("Hey, %s!", s);
    }
    return 0;
    }

<div id='text'>
They will both do the same thing. In Python, you don't have to worry about curly brackets
in syntax, except when working with dictionaries. However, Python demands to be written with 4 spaces for each indentation, and
follows strict rules for indenting.
Check it out:
</div>

    from sys import argv

    if __name__ == '__main__':
      if len(argv) >= 1:
        s = argv[1]
        print("Hey, %s!" % s)
***

<div id='text'>
Now, we could implement this Python in a different way, but we could not change the indentation even if we tried without raising an exception. It's so very intuitive to read, while demanding such an idiosyncratic syntax at the same time. Both of these examples are a simple way to write the string "Hey, _name_!" (where _name_ is the first positional argument to the program) to standard output. 
</div>
***
<div id='text'>
What's all the nonsense in the example written in C above? Well, it's a long story, and if you just write Python, you may never need to know. But learning Python will teach you the essentials of many computer programming paradigms: copy by value vs. reference, logic and flow control, object-oriented design, even basic functional programming. Because of this, Python can do more with less. 
</div>
***
<div id='text'>
There are definitely reasons to learn C, C++, or Java as a first programming language, for example, you get more familiar with the underlying data structures, learn more about resources and memory allocation (garbage collection), and overall just get more experience interacting with your operating system. I think Python is better as a first language because it introduces one to syntax, logic, and references very intuitively.
</div>
***

##Why YOU Should Learn How to Program
<div id='text'>
Its fun! :) Also there are tons of reasons for people these days to learn even just the basics of computer programming. It could even get you a pay raise. It will most definitely increase your efficiency and productivity on the computer. If you are one of those people who get frustrated easily with computers, it will also probably make you more frustrated at first, but over time you will appreciate your deeper understanding of the subject. It will allow you to sympathize with the difficulties in making an application 'user friendly'. But most importantly, writing code will allow your creative mind to flourish.
</div>

##How to Install Python
<div id='text'>
To install Python on Windows, you can go to <a target='_blank' href='https://python.org/downloads'> this </a> link and download 
the binary for the vanilla install. But if you want to install a more complete 'batteries included' distribution version of Python,
you should definitely go straight to <a target='_blank' href='http://www.continuum.io/downloads'> Anaconda </a>. Anaconda
is the same as Python, except that it comes with tons of pre-installed modules built for scientific computing, among them
matplotlib and bokeh (for plotting data), numpy, pandas, scipy, sklearn (for computing).
</div>
***