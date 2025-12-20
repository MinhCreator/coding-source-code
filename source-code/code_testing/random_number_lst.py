import random

# using random.sample()
# to generate random number list
res = [random.randrange(1, 10, 1) for i in range(100)]
 
# printing result
print ("Random number list is : " +  str(res))
