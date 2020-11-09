# while loop

`while` loop is used to perform a bunch of statements multiple times until a condition becomes `false`. 
This is commonly used to repeat something multiple times instead of copying code multiple times.
 
The structure looks something like this where
```
while <condition>:
  <statement>
  ...
```
`<condition>` is a placeholder for any boolean expression. e.g, `i < 5`, `name == 'swetha'`, `i < 5 and j > 6`

`<statement>` could be any python code. e.g, `print(name)`, `total = i+j`

e.g
```python
i = 0         # initializes variable i to 0
while i < 2:  # loop runs until i < 2
  print(i)    # prints the value in i every time it comes inside the loop
  i = i+1     # increment i and store it in i
print("done")
```
Let's go through each iteration of the loop

* step 1: `i = 0`. Store `0` in `i`
* step 2: check if `i < 2`. It evaluates to `True`, so it goes inside the loop
* step 3: print the value in `i`, which is `0`
* step 4: reads the value of `i` which is `0`, increments it and stores it in `i`. So `i` is now `1`
* step 5: check if `i < 2`. It evaluates to `True`, so it again goes inside the loop
* step 6: print the value in `i`, which is `1`
* step 7: reads the value of `i` which is `1`, increments it and stores it in `i`. So `i` is now `2`
* step 8: check if `i < 2`. It evaluates to `False`, since `2` is not less than `2`. It stops the loop.
* step 9: print `"done"` as that is the next line outside of the loop
Note that `i` is incremented in the loop. If it is not incremented, the loop condition can never evaluate to `False` and the loop will run forever.

Another e.g
```python
num = 2
while num != 1024:
  print(num)
  num = num * 2
```
output:
```
2
4
8
16
32
64
128
256
512
```

Question: How many times does the above loop run? What is the Output?
 
Answer: 9

```python
from math import *

degree = 0
while sin(radians(degree)) < 1:
  print(degree)
  degree = degree + 5
```
output
```
0
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
```
