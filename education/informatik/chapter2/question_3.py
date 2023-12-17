def question_3():
    i = 1
    s = 1
    while (True):
        s = s * i
        i = i + 3
        if i > 100:
            break
    
    print("s= %d" % s)
    print("i= %d" % i)    

if __name__=="__main__":
    question_3()