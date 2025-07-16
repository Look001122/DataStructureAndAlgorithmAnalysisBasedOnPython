import time

def sumOfN3(n):
    start=time.time()

    theSum=(n*(n+1))/2

    end = time.time()

    return theSum,end-start

for i in range(5):
 print("Sum is %d required %30.26f seconds" % sumOfN3(100000000000))