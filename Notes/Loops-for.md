# for loop

`for` is similar to `while` loop in a sense that it also does something multiple times. 
Instead of doing something until a condition becomes false(like `while` loop), it loops over data types like list or strings.

The structure looks something like
```
for <loop variable> in <iterable>
  <statement>
  ...
```
`<iterable>` could be a list / string variable or value (constant) `<loop variable>` in each iteration the loop variable contains successive value present in the iterable


e.g
```python
for i in [0,1,2]:
  print(i)
print("done")
```

Let's go through the loop

* step 1: `[0, 1, 2]` is a list, so it can be looped over(also called as iterable).
* step 2: `i` is set the value `0` automatically. Since `0` is the first item in the list.
* step 3: prints value `i` which is `0`
* step 4: `i` is set to the value `1` automatically. Since `1` is the next item in the list. Note that you don't manipulate the loop variable `i` directly
* step 5: prints value `i` which is `1`
* step 6: `i` is set to the value `2` automatically. Since `2` is the next item in the list. Note that you don't manipulate the loop variable `i` directly
* step 7: prints value `i` which is `2`
* step 8: there are no more items in the list, so the loop terminates. Note there is no explicit boolean condition like `while` loop.
* step 9: print "done"
Note that i (loop variable) acts like magic because in each iteration, the value automatically points to subsequent items in the list(iterable)

Another example

```python
for letter in "swetha":
  print(letter)
```
output
```
s
w
e
t
h
a
```

```python
count = 0
for letter in "tom and jerry":
  if letter == "a":
    count = count + 1
print(count)
```
output
```
1
```

How about this. What is the program trying to do. What will be the output?

```python
from math import *

for degree in [0, 30, 45, 60, 90]:
    print(sin(radians(degree))

```
output
```
0.0
0.49999999999999994
0.7071067811865475
0.8660254037844386
1.0
```
