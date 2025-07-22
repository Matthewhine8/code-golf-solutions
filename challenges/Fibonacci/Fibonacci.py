x=[0,1]
c=1
print(0)
print(1)
for i in range(29):
  y=x[c]+x[c-1]
  x.append(y)
  c+=1
  print(y)
