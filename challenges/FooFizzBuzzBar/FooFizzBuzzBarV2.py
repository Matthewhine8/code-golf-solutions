for i in range(1,1001):
  print("Foo"*(i%2==0)+"Fizz"*(i%3==0)+"Buzz"*(i%5==0)+"Bar"*(i%7==0)+str(i)*((i%2 and i%3 and i%5 and i%7) != 0))
