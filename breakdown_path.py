
def replace_dot_commas(text: str) -> str:
    new_text = "\n".join([s for s in text.split(";")])
    return new_text


path = input("Enter path: ")
with open("bd_text.txt", "+w") as file:
    print(replace_dot_commas(path), file=file)
