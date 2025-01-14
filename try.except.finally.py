# More on exceptions: https://docs.python.org/3/library/exceptions.html

### Basic example of 'try-except-else' ###
while True:
    try:
        eggs = int(input('How many eggs you have? '))
    except ValueError:
        print("Please use number as input.")
    else:
        break
cakes = eggs // 4
print('You can make %d %s' % (cakes, 'cake' if cakes == 1 else 'cakes'))
'''
>>> How many eggs you have? 4
>>> You can make 1 cake
>>> 
>>> How many eggs you have? asd
>>> Please use number as input.
>>> How many eggs you have? 8
>>> You can make 2 cakes
'''

### Multiple 'except' can be used ###
try:
   print(4/0)
except BufferError:
   print('except BufferError')
except ZeroDivisionError:
   print('except ZeroDivisionError')
except:
    print('Generic except')
print('Print at the end')
'''
>>> except ZeroDivisionError
>>> Print at the end
'''


try:
   print(4/0)
finally:
   print('Print on finally')
   raise
print('Print at the end')
'''
>>> Print on finally
>>> Traceback (most recent call last):
>>>   File "/Users/aski/Learn/simple.py", line 38, in <module>
>>>     print(4/0)
>>> ZeroDivisionError: division by zero

  If a finally clause is present, the finally clause will execute as the last task before the try statement completes. 
  The finally clause runs whether or not the try statement produces an exception. Useful for clean-up handling.

'''
