# Dictionary

[Tutorial video](https://www.youtube.com/watch?v=XCcpzWs-CI4)

```
>>> counts = {"apple":1, "banana": 2}
>>> counts
{'apple': 1, 'banana': 2}
>>> counts["apple"]
1
>>> counts["apple"] = 3
>>> counts
{'apple': 3, 'banana': 2}
>>> for i in counts:
...     print(i)
...
apple
banana
>>> for i in counts:
...     print(counts[...     print(coun
KeyboardInterrupt
>>>
>>>
>>>
>>> for i in counts:
...     print(i)
...
apple
banana
>>> for i in counts:
...     print(counts[i])
...
3
2
>>> for i in counts:
...     print(i,counts[i])
...
('apple', 3)
('banana', 2)
>>> count["potato"] = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'count' is not defined
>>> counts["potato"] = 100
>>> counts
{'potato': 100, 'apple': 3, 'banana': 2}
>>> for i in counts:
...     print(i,counts[i])
...
('potato', 100)
('apple', 3)
('banana', 2)
>>> for i in counts:
...     counts["tomato"] = 1
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
>>> for i in counts:
...     counts["apple"] = 1
...
>>> counts
{'tomato': 1, 'potato': 100, 'apple': 1, 'banana': 2}
>>> len(counts)
4
>>> for i in range(len(counts))
  File "<stdin>", line 1
    for i in range(len(counts))
                              ^
SyntaxError: invalid syntax
>>> for i in range(len(counts)):
...     print(i)
...
0
1
2
3
>>> for i in range(len(counts)):
...     counts[i]
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyError: 0
>>> counts
{'tomato': 1, 'potato': 100, 'apple': 1, 'banana': 2}
>>> counts[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> numbers = {0:"apple", 1:"banana"}
>>> numbers
{0: 'apple', 1: 'banana'}
>>> for i in range(len(numbers))
  File "<stdin>", line 1
    for i in range(len(numbers))
                               ^
SyntaxError: invalid syntax
>>> for i in range(len(numbers)):
...     print(numbers[i])
...
apple
banana
>>> ingredients = {'dosa':['batter','chutney']}
>>> ingredients
{'dosa': ['batter', 'chutney']}
>>> ingredients['dosa']
['batter', 'chutney']
>>> ingredients['dosa'].append('sambar')
>>> ingredients
{'dosa': ['batter', 'chutney', 'sambar']}
>>> ingredients['idly'].append('urad dal')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'idly'
>>> ingredients['idly'] = 'batter'
>>> ingredients['idly'].append('urad dal')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'append'
>>> ingredients
{'dosa': ['batter', 'chutney', 'sambar'], 'idly': 'batter'}
>>> ingredients['idly'] = ['batter']
>>> ingredients
{'dosa': ['batter', 'chutney', 'sambar'], 'idly': ['batter']}
>>> ingredients['idly'].append('urad dal')
>>> ingredients
{'dosa': ['batter', 'chutney', 'sambar'], 'idly': ['batter', 'urad dal']}
>>> >>> for i in counts:
...     ingredients[i] = ['dummy']
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'countsunts' is not defined
>>> for i in counts:
...     ingredients[i] = ['dummy']
...
>>> ingredients
{'tomato': ['dummy'], 'apple': ['dummy'], 'potato': ['dummy'], 'dosa': ['batter', 'chutney', 'sambar'], 'idly': ['batter', 'urad dal'], 'banana': ['dummy']}
```
