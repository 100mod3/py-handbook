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
The finally clause runs whether or not the try statement produces an exception. Useful for clean-up.
'''
