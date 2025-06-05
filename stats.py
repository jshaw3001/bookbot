def word_count(filepath):
    with open(filepath) as f:
        text = f.read()
    lst = text.split()
    return str(len(lst))

def char_count(filepath):
    chars = {}
    with open(filepath) as f:
        text = f.read()
    for x in text.lower():
        if x in chars:
            chars[x] += 1
        else:
            chars.update({x:1})
    return chars

def sort_on(dict):
    return dict["num"]

def dict_sort(filepath):
    count = []
    chars = char_count(filepath)
    lst = []
    for x in chars:
        if x.isalpha():
            count.append({"char": x, "num": chars[x]})
    count.sort(reverse=True, key=sort_on)
    for y in count:
        lst.append(y.get("char") + ": " + str(y.get("num")))
    return lst
    
