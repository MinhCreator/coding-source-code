import random

def random_color_hex():
    hex_col_def = "#"
    
    for i in range(6):
        hex_col_def += random.choice("0123456789ABCDEF")

    return hex_col_def

def random_color_rgba():

    R = random.randint(0, 256)
    G = random.randint(0, 256)
    B = random.randint(0, 256)
    A = round(random.uniform(0, 1), 2)


    return "rgba(" + str(R) + "," + str(G) + "," + str(B) + "," + str(A) + ")"

# print(random_color_rgba())

def random_color_hsl():

    H = random.randint(0, 360)
    S = random.randint(0, 101)
    L = random.randint(0, 101)

    return "hsl(" + str(H) + "," + str(S) + "%," + str(L) + "%)"

# print(random_color_hsl())

path = "./thử nghiệm code/color.txt"

with open(path, "w") as file:
    
    hex = "\n" + "\n".join([random_color_hex() for _ in range(10)])
    rgba = "\n" + "\n".join([random_color_rgba() for _ in range(10)])
    hsl = "\n" + "\n".join([random_color_hsl() for _ in range(10)])
    results = ("--Hex Color:" + hex) + ("\n\n--RGBA Color:" + rgba) + ("\n\n--HSL Color:" + hsl) 

    print(results, file = file)
    