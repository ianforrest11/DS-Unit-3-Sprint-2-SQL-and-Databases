Last login: Wed Sep 11 10:43:38 on ttys001
(base) Ians-MBP:~ ianforrest$ python
Python 3.7.3 (default, Mar 27 2019, 16:54:48) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> def increment(x):
... return x + 1
  File "<stdin>", line 2
    return x + 1
         ^
IndentationError: expected an indented block
>>> def increment(x):
...     return x + 1
... 
>>> def double(x):
...   return 2 * x
... 
>>> increment(10)
11
>>> double(10)
20
>>> def run_twice(func, arg):
...   return func(func(arg))
... 
>>> run_twice(increment,10)
12
>>> run_twice(double, 10)
40
>>> for i in range(10):
...   print(i)
... 
0
1
2
3
4
5
6
7
8
9
>>> def rec_print(x):
...   print
... 
>>> for i in range(10, 0):
...   print(i)
... 
>>> def rec_print(n):
...   print(n)
...   if n >= 0:
...     rec_print(n - 1)
... 
>>> for i in range(10, 0, -1):
...   print(i)
... 
10
9
8
7
6
5
4
3
2
1
>>> rec_print(10)
10
9
8
7
6
5
4
3
2
1
0
-1
>>> map
<class 'map'>
>>> increment
<function increment at 0x10fed27b8>
>>> help(map)

>>> map(increment, [1, 2, 3, 4])
<map object at 0x10fec95f8>
>>> list(map(increment, [1, 2, 3, 4]))
[2, 3, 4, 5]
# map applies a function to an iterable, applies it elementwise, returning
# another iterable of the same length

>>> reduce
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reduce' is not defined
>>> from functools import reduce
>>> def add(x, y):
...   return x + y
... 
>>> add(1,2)
3
>>> reduce(add, [1,2,3,4])
10
>>> add(add(add(1, 2), 3), 4)
10
>>> # Big finish - MapReduce!
... 
>>> def identity(x):
...   return x
... 
>>> map(identity, [1,2,3,4])
<map object at 0x110172390>
>>> list(map(identity, [1,2,3,4]))
[1, 2, 3, 4]
>>> map_results = map(identity, [1,2,3,4])
>>> reduce(add, map_results)
10
>>> 
