Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[0])
print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))

# Code: http://www.py4e.com/code3/party1.py
SyntaxError: multiple statements found while compiling a single statement
>>> class PartyAnimal
SyntaxError: invalid syntax
>>> class PartyAnimal
SyntaxError: invalid syntax
>>> class PartyAnimalls
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> >>> stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[0])
print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))>>> stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[0])
print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))
SyntaxError: invalid syntax
>>> class PartyAnimal
SyntaxError: invalid syntax
>>> x = 0
>>> an = 900
>>> vars(an)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    vars(an)
TypeError: vars() argument must have __dict__ attribute
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 0, 'an': 900}
>>> an()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    an()
TypeError: 'int' object is not callable
>>> vars(an)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    vars(an)
TypeError: vars() argument must have __dict__ attribute
>>> 
