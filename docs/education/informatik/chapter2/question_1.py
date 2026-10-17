def question_1():
    a = 0
    b = 1
    while b <= 20:
        a = a + b
        b = b + a
    
    print(a)
    print(b)


if __name__=="__main__":
    question_1()