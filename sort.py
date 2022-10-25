def get_da(n, f):
    list=[]
    for i in f:
        list.append(i.split()[n])
    return list


def sort(n, f):
    li=[]
    for i in f:
        if n in i:
            li.append(i)
    return li    