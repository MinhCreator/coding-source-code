#def ucln(a, b):
#    while b != 0:
#        r = a % b
#        a = b
#        b = r
#    return a

#open_file = open("ucln\CAPSO.INP", "r")
#read_file = open_file.read()
#open_file.close()
#lst = read_file.split("\n")
#open_file2=open("ucln\CAPSO.OUT", "w")
#for i in lst:
#    s = i.split(" ")
#    a, b = map(int, s)
#    ham = ucln(a, b)
#    write_file = open_file2.write(str(ham) + "\n")
#open_file2.close()



def ucln(a,b):
    tmp = a 
    tmp1 = b
    while tmp != tmp1:
        if tmp > tmp1:
            tmp -= tmp1
        else:
            tmp1 -= tmp
    return 'ước chung lớn nhất: ' + str(tmp)

a , b = int(input('nhập a: ')), int(input('nhập b: '))
print(ucln(a,b))