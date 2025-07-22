for i in range(1,1001):
  x=''
  if i%2==0:
    x+='Foo'
  if i%3==0:
    x+='Fizz'
  if i%5==0:
    x+='Buzz'
  if i%7==0:
    x+='Bar'
  if (i%2 and i%3 and i%5 and i%7) != 0:
    x+=str(i)
  print(x)
