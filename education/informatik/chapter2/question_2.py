def question_2():
    x = int(input("Please enter x = "))
    i = 0
    m = 0
    k = 1
    while i < 5:
        if i > 2:
            k = k + x
        else:
            m = m + k
        i = i + 1
        k = k + 1

    print("k= %d" % k)
    print("m= %d" % m)


if __name__=="__main__":
    question_2()