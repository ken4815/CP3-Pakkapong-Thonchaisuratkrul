high = int(input("High(number):"))
for i in range(high):
   high = high - 1
   print(" " * high, "*" * ((i*2)+1))