import math 

def sohoanhao(n):
    d = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            d += i
    if d == n:
            return True
    return False

def so_nguyen_to(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    elif n == 0 or n == 1:
        return False
    else:
        k = 5
        can = math.sqrt(n)
        tmp = math.floor(can)
        while k <= tmp:
            if n % k == 0 or n % (k + 2) == 0:
                return False
            k += 6
    return True

file = open('thử nghiệm code\SN.inp', 'r')
read = file.read()
file.close()
lst = list(map(int, read.split('\n')))
file_nt = open('NT.out', 'w')
file_hh = open('HH.out', 'w')
for i in lst:
    if sohoanhao(i) == True:
        file_hh.write(str(i) + '\n')
    elif so_nguyen_to(i) == True:
        file_nt.write(str(i) + '\n')
file_nt.close()
file_hh.close()
import time 

start = time.time()

for i in range(1000000):
    pass

end = time.time()
print('time running file: ', round(end - start,1))