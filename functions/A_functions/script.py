def ends_with_t(str):
    n = len(str)
    if str[n-1] == "t":
        print("True")
        return True
    else:
        print("False")
        return False

ends_with_t("hdwgvwsbdhcgdhsh")


def average(n1,n2,n3):
    sum =  n1 + n2 +n3
    return sum/3

print(average(5,8,2))

