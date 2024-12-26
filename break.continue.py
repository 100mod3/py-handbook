# The break statement terminates for/while loop completely. If nested, It affects only current, innermost loop.

for n in ['a', 'b', 'c', 'd', 'e']:
   for k in [1, 2, 3, 4, 5]:
       if k == 3:
           break
       print('%s%s' % (n, k), end=' ')
# >>> a1 a2 b1 b2 c1 c2 d1 d2 e1 e2

for n in ['a', 'b', 'c', 'd', 'e']:
   for k in [1, 2, 3, 4, 5]:
       if k == 3:
           continue
       print('%s%s' % (n, k), end=' ')
# >>> a1 a2 a4 a5 b1 b2 b4 b5 c1 c2 c4 c5 d1 d2 d4 d5 e1 e2 e4 e5
