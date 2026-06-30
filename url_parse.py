import re

def find_match(pattern, url) :

    if pattern in url :
        return url
    
    else: return ''



with open('C:\\Users\\Administrator\\Desktop\\vivaldi-bro.txt', 'r') as f:

    out_lst = [find_match('godot', line) for line in f if find_match('godot', line) != '']

    with open('./result.txt', 'w') as file:
        file.write(''.join(out_lst))
        print(len(out_lst))
