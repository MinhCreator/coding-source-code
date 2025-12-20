from math import sqrt, floor

# check if a number is prime
def prime(number: int) -> bool:
    if number == 2 or number == 3: 
        return True

    elif number == 1 or number % 2 == 0 or number % 3 == 0: 
        return False
        
    elif number == 0: return False
    
    else:
        k = 5
        t = sqrt(number)
        tmp = floor(t)
        
        while k <= tmp:
            if number % k == 0 or number % (k + 2) == 0:
                return False
            k += 6
                
    return True

# check if a number is super prime
def super_prime(n) -> bool:
    
    if not prime(n): 
        return False
        
    elif prime(n) == True:
        digits = [int(s) for s in str(n)]
        
    for digit in digits:
        
        if prime(digit) == True:
            return True

        elif not prime(digit):
            return False

# chuyển số la mã thành số nguyên
def covert_roman_to_int(s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for i in range(len(s) - 1):

        if roman[s[i]] < roman[s[i + 1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]

    return result + roman[s[-1]]

# tìm một char trong str
def find_funique_char(text: str) -> int:
    for index, char in enumerate(text):
        if text.count(char) == 1:
            return index
    return -1

# kiểm tra số đối xứng 
def isPalindrome(number: int) -> bool: 

    x_to_str = str(number)

    if x_to_str == x_to_str[::-1]:
        return True
    else:
        return False
    
# xóa các số trùng lặp trong list
def remove_duplicate(lists_number: list[int]) -> int:
    store = 0

    for number in range(1, len(lists_number)):

        if lists_number[store] != lists_number[number]:
            store += 1

            lists_number[store] = lists_number[number]

    return store + 1 

# xóa element được chỉ định trong list
def remove_ele( lists_number: list[int], value: int) -> int:

    # var để theo dõi số lượng phần tử không bằng  val
    tracker = 0

    for inter in range(len(lists_number)):
        if lists_number[inter] != value:
            # nếu num hiện tại không bằng val
            # di chuyển phần tử hiện tại đến pos tiếp theo
            lists_number[tracker] = lists_number[inter]
            tracker += 1
            
    return tracker

# tìm số được chỉ định trong list
def search_insert(lists_number: list[int], target: int) -> int:
    left, right = 0 , len(lists_number) - 1

    while left <= right:
        middle = (left + right) // 2
        
        if lists_number[middle] == target:
            return middle
            
        elif lists_number[middle] < target:
            left = middle + 1
            
        else:
            right = middle - 1
            
    return left

# kiểm tra các bracket hợp lệ trong str
def isValid(store: str) -> bool:

    stack = []
    bracket = {'(': ')', '[': ']', '{': '}'}

    for char in store:
        
        if char in bracket.keys():
            stack.append(char)
            
        elif char in bracket.values():

            if not stack or bracket[stack.pop()] != char:
                return False
                
        else:
            return False
        
    return len(stack) == 0

# kiểm tra số đối xứng
def is_perfect_num(number: int) -> bool:

    sums = 0

    for num in range(1, number//2 + 1):

        if number & num == 0:
            sums += num

    if sums == number:
        return True

    return False

# check time running code
import time 
def run_code():
    start = time.time()

    for i in range(1000000):
        pass

    end = time.time()

    return 'time running file: ' + str(round(end - start,1))

    