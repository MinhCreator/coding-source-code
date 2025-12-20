def add_elements(num: int, lists: list):

    tmp_list = []

    for num_k in range(len(lists) + 1):
        list = lists.copy()
        list.insert(num_k, num)
        tmp_list.append(list)

    return tmp_list
    
def generate_permutation(num: int):

    if num == 1: return [[num]]
    
    lst_permutation = []

    before_func = generate_permutation(num - 1)

    for element in before_func:
        lst_permutation += add_elements(num, element)

    return lst_permutation

#print(generate_permutation(5))


def permutation_dictionary(lists: list, num: int):
   
   #find max j in right

   right = num - 2

   while right >= 0 and lists[right] >= lists[right + 1]:
      
      right -= 1
      
      if right == -1: return None

   #find max k in right j

   right_k = num - 1

   while lists[right] >= lists[right_k]: 
        right_k -= 1    

   lists[right], lists[right_k] = lists[right_k], lists[right] 
   lists[right + 1:num] = lists[num - 1:right : - 1]
   return lists

def in_permutation(lists: list):
   
   length = len(lists)
   result = True

   while result:
       print(lists)
       lists = permutation_dictionary(lists, length)
       result = lists != None

n = 4
list = [1, 2, 3, 4]
in_permutation(list)


   