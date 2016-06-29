#coding:utf-8

def Arrange (num):
    out = ''
    list = []
    for i in reversed(xrange(61)):
        for j in reversed(xrange(61)):
            for k in reversed(xrange(61)):

                if i + j + k == num:
                    throw = [i,j,k]
                    throw.sort(reverse=True)
                    #print throw
                    '''
                    if not (throw[-1] % 2 == 0 and throw[-1] <= 50):
                        tmp = throw[-1]
                        throw[-1] = throw[-2]
                        throw[-2] = tmp

                    '''
                    if throw not in list:
                        list.append(throw)

    print check(list)
    #print list
    #print num, list[0]
                    #print num, Area(i), Area(j), Area(k), i, j, k

def check (throws):
    double = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,50]
    for i in xrange(0,len(throws)):
        throw = throws
        if throw[-1] in double:
            return throw

def Area (num):
    if num < 21:
        return str(num)
    elif num == 50:
        return "DB"
    else:
        if num % 3 == 0:
            return "T"+str(num/3)
        elif num % 2 == 0:
            return "D"+str(num/2)
        else:
            return "ありません" + str(num)


if __name__ == "__main__":
    #for i in xrange(5):
    Arrange(170)
