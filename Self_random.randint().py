import datetime
import sys
'''USED CURRENT TIME CONCEPT TO GENERATE DIFFERENT NUMBERS
JUS AS random>randint() DOES WITHOUT USING random MODULE'''
def apna_rndm(mn,mx):
    l=[]
    for j in range(mn,mx+1):
        l.append(j)
    if (mn == mx) :
        print('The number is:')
        print(mn)
        sys.exit()
    # STORED CURRENT TIME IN VARIABLE cdt
    cdt = datetime.datetime.now()
    mx = len(l)
    s1 = 0
    if (mx<15):
        i = 2*cdt.second
        if (i >= mx) :
            while (i != 0) :
                r = i % 10
                s1 += r
                i = i // 10
            if (s1 < mx) :
                print('The number is:')
                print(l[s1])
                sys.exit()
            elif (s1 > (2 * mx)) :
                print('The number is:')
                print(l[s1 - (2 * mx)])
                sys.exit()
            else :
                h = cdt.hour
                if (h < mx) :
                    print('The number is:')
                    print(l[h])
                    sys.exit()
                else :
                    print('The number is:')
                    print(l[mx - h])
                    sys.exit()
        else :
            print('The number is:')
            print(l[i])
            sys.exit()
    else:
        i = cdt.microsecond
        if (i >= mx) :
            while (i != 0) :
                r = i % 10
                s1 += r
                i = i // 10
            if (s1 < mx) :
                print('The number is:')
                print(l[s1])
                sys.exit()
            elif (s1 > (2 * mx)) :
                print('The number is:')
                print(l[s1 - (2 * mx)])
                sys.exit()
            else :
                h = cdt.hour
                if (h < mx) :
                    print('The number is:')
                    print(l[h])
                    sys.exit()
                else :
                    print('The number is:')
                    print(l[mx - h])
                    sys.exit()
        else :
            print('The number is:')
            print(l[i])
            sys.exit()
# RUN JUST BY CALLING apna_rndm(var1,var2); var1>var2
# LIMITATIONS ONLY WORKS ON INTEGRAL INPUTS AND NOT ON FLOATING POINT DECIMALS
