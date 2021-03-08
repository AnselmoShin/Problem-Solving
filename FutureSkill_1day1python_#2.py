def all_unique(lst):
    hash = dict()
    flag = False
    for each in lst:
        try:
            if hash[each]:
                flag = True
                break
        except:
            hash[each] = True
    if flag:
        print(False)
    else:
        print(True)

all_unique([1, 2, 3, 4, 5, 6])
all_unique([1, 2, 2, 3, 4, 5])