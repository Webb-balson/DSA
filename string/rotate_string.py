def rotate_string(str):
    l = len(str)

    for i in range(l):
        t1 = str[i:]
        t2 = str[:i]

        print(t1+t2)

s = "geeks"
rotate_string(s)