from math import floor, sqrt

def prime(number: int) -> bool:
    if number == 2 or number == 3:
        return True 
    elif number == 1 or number % 2 == 0 or number % 3 == 0:
        return False
    else:
       k = 5 
       can = sqrt(number)
       lam_tron_xuong = floor(can)
       while k <= lam_tron_xuong:
           if number % k == 0 or number % (k + 2) == 0:
               return False
           k += 6
    return True


def super_prime(number: int) -> bool:
    if not prime(number):
        return False
    else:
        while number > 0 :
            if not prime(number):
                return False
            number //= 10
    return True


def kt_đối_xứng(number: int) -> bool:
    # flag = True => số đối xứng
    # flag = False => không phải số đối xứng
    flag = False
    if ( str(number)[::-1] == str(number)):
      flag = True
    return flag


def find_the_next_super_prime(number: int) -> int:
    #sàng số nguyên tố  
    tmp = 1000000
    t = [True] * tmp
    for i in range(2, tmp // 2+1 ):
        for w in range(i * 2, tmp, i):
            t[w] = False
    
    #list số nguyên tố từ n => 1000000
    tmp2 = []
    for a in range(2, tmp):
        if t[a]:
            tmp2.append(a)
    #tìm số nguyên tố lớn hơn n và số nguyên tố đó phải là số đối xứng
    for i in tmp2:
        if i > number and kt_đối_xứng(i) == True:
            return i


def tìm_số_siêu_nguyên_tố_đối_xứng(n):
    t = []
    tmp = 1000000
    for i in range(2, tmp // 2 + 1):
        if prime(i) == True:
            t.append(i)
    for a in t:
        if a > n and kt_đối_xứng(a) == True:
            return a

n = open("PRPA.inp", 'r')
doc = n.read()
t = doc.split('\n')
n.close()
n2 = open("PRPA.out", 'w')
for i in t:
   #t = find_the_next_super_prime(int(i))
   t = tìm_số_siêu_nguyên_tố_đối_xứng(int(i))
   n2.write(str(t))
   n2.write('\n')

n2.close()



