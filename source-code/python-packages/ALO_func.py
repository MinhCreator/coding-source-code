from math import sqrt, floor

# check if a number is prime
def prime(number: int) -> bool:
    """
    Check if a given number is a prime number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
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
    """
    Check if a number is a super prime.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if it meets the criteria, False otherwise.
    """
    
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
    """
    Convert a Roman numeral string to an integer.

    Args:
        s (str): The Roman numeral string.

    Returns:
        int: The integer representing the Roman numeral.
    """
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
    """
    Find the index of the first unique character in a string.

    Args:
        text (str): The string to search.

    Returns:
        int: The index of the first unique character, or -1 if no unique character exists.
    """
    for index, char in enumerate(text):
        if text.count(char) == 1:
            return index
    return -1

# kiểm tra số đối xứng 
def isPalindrome(number: int) -> bool: 
    """
    Check if an integer is a palindrome.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """

    x_to_str = str(number)

    if x_to_str == x_to_str[::-1]:
        return True
    else:
        return False
    
# xóa các số trùng lặp trong list
def remove_duplicate(lists_number: list[int]) -> int:
    """
    Remove duplicated numbers in an array in-place and return the new length.

    Args:
        lists_number (list[int]): A list of integers.

    Returns:
        int: The new length of the list containing unique elements.
    """
    store = 0

    for number in range(1, len(lists_number)):

        if lists_number[store] != lists_number[number]:
            store += 1

            lists_number[store] = lists_number[number]

    return store + 1 

# xóa element được chỉ định trong list
def remove_ele( lists_number: list[int], value: int) -> int:
    """
    Remove all occurrences of a specified value from a list in-place.

    Args:
        lists_number (list[int]): The list from which to remove elements.
        value (int): The value to remove.

    Returns:
        int: The new length of the list after removal.
    """

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
    """
    Search for a target value in a sorted list. If found, return its index.
    If not found, return the index where it would be if inserted in order.

    Args:
        lists_number (list[int]): A sorted list of integers.
        target (int): The value to search for.

    Returns:
        int: The index of the target or its insertion position.
    """
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
    """
    Check if a string of brackets is perfectly matched and valid.

    Args:
        store (str): A string containing types of brackets.

    Returns:
        bool: True if the brackets are validly closed, False otherwise.
    """

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
    """
    Check if a number is a perfect number (sum of its proper divisors equals the number).

    Args:
        number (int): The number to check.

    Returns:
        bool: True if it is a perfect number, False otherwise.
    """

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
    """
    Measure and return the execution time of a specific block of code.

    Returns:
        str: A string formatted with the runtime in seconds.
    """
    start = time.time()

    for i in range(1000000):
        pass

    end = time.time()

    return 'time running file: ' + str(round(end - start,1))


    