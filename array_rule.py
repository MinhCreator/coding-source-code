# ranges = 10
# lst = [0] * ranges 
# lst[0] = 1
# plus = 1
# step = 1
# for i in range(1, ranges, step):
#     plus += 1
#     lst[i] = lst[i - 1] + plus + 1
# # 
# print(lst)

def phanTichSoNguyen(n):
    i = 2;
    listNumbers = [];
    # phân tích
    while (n > 1):
        if (n % i == 0):
            n = int(n / i);
            listNumbers.append(i);
        else:
            i = i + 1;
    # nếu listNumbers trống thì add n vào listNumbers
    if (len(listNumbers) == 0):
        listNumbers.append(n);
    return listNumbers;

print(phanTichSoNguyen(100))
