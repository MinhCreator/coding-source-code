
import time 

start = time.time()

for i in range(1000000):
    pass

end = time.time()
print('time running file: ', round(end - start,1))
