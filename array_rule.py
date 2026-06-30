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

def phanTichSoNguyen(number : int) -> list[int]:
    i: int = 2;
    listNumbers = []
    # phân tích
    while (number > 1):
        if (number % i == 0):
            n = int(number / i);
            listNumbers.append(i);
        else:
            i = i + 1;
    # nếu listNumbers trống thì add n vào listNumbers
    if (len(listNumbers) == 0):
        listNumbers.append(number);
    return listNumbers;

print(phanTichSoNguyen(100))

    
