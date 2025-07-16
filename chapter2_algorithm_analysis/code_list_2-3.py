import time

def sumOfN2(n):
    start=time.time()

    theSum=0
    for i in range(1,n+1):
        theSum += i

    end = time.time()

    return theSum,end-start

for i in range(5):
 print("Sum is %d required %15.12f seconds" % sumOfN2(1000000))