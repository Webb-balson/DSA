def string_concatanate(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    str3 = [0]*(l1+l2)
    for i in range(l1):
        str3[i] = str1[i]

    x = 0
    for i in range(l1, l1+l2):
        str3[i] = str2[x]
        x += 1

    print("".join(str3))

str1 = "Balson"
str2 = "Gorai"
string_concatanate(str1,str2)