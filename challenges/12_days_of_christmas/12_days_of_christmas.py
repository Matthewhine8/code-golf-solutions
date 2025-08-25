x=['A Partridge in a Pear Tree','Two Turtle Doves','Three French Hens','Four Calling Birds','Five Gold Rings','Six Geese-a-Laying','Seven Swans-a-Swimming','Eight Maids-a-Milking','Nine Ladies Dancing','Ten Lords-a-Leaping','Eleven Pipers Piping','Twelve Drummers Drumming']
y=['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Ninth','Tenth','Eleventh','Twelfth']
for i in range(12):
  j=i
  print('On the {} day of Christmas\nMy true love sent to me'.format(y[i]))
  while j>=0:
    if j==0:
      print(x[j]+'.\n')
    if j>0 and j!=1:
      print(x[j]+',')
    if j==1:
      print(x[j]+', and')
    j=j-1
