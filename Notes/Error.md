# Errors

[Tutorial](https://docs.python.org/3/tutorial/errors.html)

* 1/0 => ZeroDivisionError
* name => NameError (name variable not defined previously)
* \[1,2,3\][3] => IndexError (accessing index of list > length)

```
try: 
  some statements
except SomeException:
  handle the exception
```

```python
try:
  dictionary = set()
  dictionary["name"]
  print(dictionary)
except KeyError:
  print("key was not found")
except NameError:
  print("name error")
except ZeroDivisionError:
  print("divide by zero error")
print("done with error")

```
