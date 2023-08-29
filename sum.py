def sum(n):

  
  partialSum = 0
  for i in range(0, n+1):
    partialSum += i*i*i
  return partialSum

print(sum(10))
